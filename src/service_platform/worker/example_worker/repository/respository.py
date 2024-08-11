from service_platform.runtime.settings import logger
from service_platform.service.postgres.lifetime import init_postgres_worker


class ExampleWorkerRepository:
    def __init__(self):
        self.database = init_postgres_worker()

    async def handler(
        self,
    ) -> None:
        try:
            # Handle the worker repository
            pass
        except Exception as e:
            logger.error(e)
        finally:
            await self.database.close()
