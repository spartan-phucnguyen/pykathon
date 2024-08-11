from datetime import datetime

from sqlalchemy import UUID, Column, DateTime, MetaData, String, Table, func
from sqlalchemy.orm import Mapped

from service_platform.db.base_table import BaseTable

UserTable = Table(
    "users",
    MetaData(),
    Column("id", UUID, primary_key=True),
    Column("email", String),
    Column("name", String),
    Column("picture_url", String),
    Column("logged_in_at", DateTime(timezone=True), server_default=func.now()),
    Column("roles", String),
    Column("auth_id", String),
    Column("auth_provider", String),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
    Column("deleted_at", DateTime),
)


class UserEntity(BaseTable):
    __tablename__ = "users"

    email: Mapped[str]
    name: Mapped[str]
    picture_url: Mapped[str]
    logged_in_at: Mapped[datetime]
    roles: Mapped[str]
    auth_id: Mapped[str]
    auth_provider: Mapped[str]
