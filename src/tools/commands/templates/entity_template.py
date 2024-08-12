from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from service_platform.db.base_class import Base
import uuid

class {name}Entity(Base):
    __tablename__ = '{plural_name}'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
