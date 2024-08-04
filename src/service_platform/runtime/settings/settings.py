import logging
import os

from pydantic_settings import SettingsConfigDict, YamlConfigSettingsSource
from pydantic_settings_yaml import YamlBaseSettings  # type: ignore
from yarl import URL

from service_platform.runtime.settings import (
    Auth0Config,
    AWSConfig,
    DBConfig,
    GoogleConfig,
    JWTConfig,
    LinkedinConfig,
    RedisConfig,
    ServerConfig,
    ZoomConfig,
)
from service_platform.utils.file_utils import get_yaml_config


class Settings(YamlBaseSettings):
    """
    Application settings.

    These parameters can be configured
    with yaml config.
    """

    _environment = str(
        (
            os.environ.get("ENVIRONMENT")
            if os.environ.get("ENVIRONMENT") is not None
            else "local"
        ),
    )

    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        secrets_dir="/",
        yaml_file=get_yaml_config(_environment),
    )

    server: ServerConfig
    postgres: DBConfig
    redis: RedisConfig
    google: GoogleConfig
    linkedin: LinkedinConfig
    zoom: ZoomConfig
    auth0: Auth0Config
    aws: AWSConfig
    jwt: JWTConfig

    @property
    def environment(self):
        return self._environment

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        # priority env variables higher than yaml files
        return (
            env_settings,
            init_settings,
            YamlConfigSettingsSource(settings_cls),
            dotenv_settings,
            file_secret_settings,
        )

    @property
    def redis_url(self) -> URL:
        """
        Assemble REDIS URL from settings.

        :return: redis URL.
        """
        return URL.build(
            scheme="redis",
            host=self.redis.address,
            port=self.redis.port,
            user=self.redis.username,
            password=self.redis.password,
            path=f"/{self.redis.base}",
        )

    @property
    def postgres_url(self) -> URL:
        """
        Assemble POSTGRES URL from settings.

        :return: postgres URL.
        """
        return URL.build(
            scheme="postgresql+asyncpg",
            host=self.postgres.address,
            port=self.postgres.port,
            user=self.postgres.username,
            password=self.postgres.password,
            path=f"/{self.postgres.db_name}",
        )


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
settings = Settings()
# logger.info("settings: {}".format(settings.model_dump()))
