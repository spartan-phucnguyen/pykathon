import uuid

import nest_asyncio  # type: ignore
from sqlalchemy import insert

from service_platform.db.user.table import UserTable

nest_asyncio.apply()


def main() -> None:
    # log_config = config_logging()
    # uvicorn.run(
    #     "service_platform.api.application:get_app",
    #     workers=settings.server.workers_count,
    #     host=settings.server.address,
    #     port=settings.server.port,
    #     reload=settings.server.reload,
    #     log_level=settings.server.uvicorn_log_level,
    #     log_config=log_config,
    #     proxy_headers=settings.server.proxy_headers,
    #     forwarded_allow_ips=settings.server.forwarded_allow_ips,
    #     loop="asyncio",
    #     factory=True,
    # )
    # test #9376
    d1: dict[str, str] = {
        "id": str(uuid.uuid4()),
        "email": "phuc@123",
        "name": "cukhoaimon",
        "picture_url": "https://www.phuc.com",
        "roles": "",
        "auth_id": "",
        "auth_provider": "",
    }
    stmt1 = insert(UserTable).values(d1)
    print(stmt1)


if __name__ == "__main__":
    main()
