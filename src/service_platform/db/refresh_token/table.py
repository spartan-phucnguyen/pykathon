from sqlalchemy import UUID, Column, Table, MetaData, TIMESTAMP
from sqlalchemy.orm import Mapped

from service_platform.db.base_table import BaseTable

table_name = "refresh_tokens"

RefreshTokenTable = Table(
    table_name,
    MetaData(),
    Column("id", UUID, primary_key=True),
    Column("user_id", UUID),
    Column("created_at", TIMESTAMP),
    Column("updated_at", TIMESTAMP),
    Column("deleted_at", TIMESTAMP),
)


class RefreshTokenEntity(BaseTable):
    __tablename__ = table_name

    user_id: Mapped[UUID]
