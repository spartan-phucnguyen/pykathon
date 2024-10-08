from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from service_platform.service.postgres.lifetime import init_postgres_worker


async def get_db_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    """
    Create and get database session.

    :param request: current request.
    :yield: database session.
    """
    session: AsyncSession = request.app.state.db_session_factory()

    try:  # noqa: WPS501
        yield session

    finally:
        await session.commit()
        await session.close()


async def get_db_session_worker() -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = init_postgres_worker()

    try:  # noqa: WPS501
        yield session

    finally:
        await session.commit()
        await session.close()
