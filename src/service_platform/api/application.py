import asyncio
import typing
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware
from yarl import URL

from service_platform.api.controller.router import api_router
from service_platform.api.lifetime import (
    register_shutdown_event,
    register_startup_event,
    register_worker,
)
from service_platform.core.exception_handler import (
    http_exception_handler,
    request_validation_exception_handler,
    unicorn_exception_handler,
)
from service_platform.core.middleware.authentication import (  # type: ignore
    AuthenticationMiddleware,
    include_public_paths,
    include_refresh_token_paths,
)
from service_platform.runtime.settings import settings
from service_platform.service.postgres.lifetime import (
    init_postgres,
    shutdown_postgres,
)
from service_platform.service.redis.lifetime import init_redis, shutdown_redis


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """

    # lifespan for app
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # on start up
        if settings.redis.enabled:
            init_redis(app)
        if settings.postgres.enabled:
            init_postgres(app)

        await register_startup_event()

        worker_task = asyncio.create_task(register_worker())

        yield
        # on shutdown
        await register_shutdown_event()
        if settings.redis.enabled:
            await shutdown_redis(app)
        if settings.postgres.enabled:
            await shutdown_postgres(app)

        worker_task.cancel()
        try:
            await worker_task
        except asyncio.CancelledError:
            pass

    app = FastAPI(
        title="service_platform",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=ORJSONResponse,
        exception_handlers={
            RequestValidationError: request_validation_exception_handler,
            HTTPException: http_exception_handler,
            Exception: unicorn_exception_handler,
        },
        lifespan=lifespan,
    )

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")

    public_paths = {URL("/docs"), URL("/openapi.json")}
    refresh_token_paths: set[typing.Any] = set()

    include_public_paths(api_router, public_paths)
    include_refresh_token_paths(api_router, refresh_token_paths)

    app.add_middleware(
        AuthenticationMiddleware,
        public_paths=public_paths,
        refresh_token_paths=refresh_token_paths,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.server.allowed_origin.split(","),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=[
            "Origin",
            "Content-Type",
            "Accept",
            "Authorization",
            "Cookie",
        ],
    )

    return app
