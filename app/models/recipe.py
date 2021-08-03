from sqlalchemy import Column, String, DateTime
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID


class Recipe(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String)
    created_by = Column(String)
    description = Column(String)
    date_created = Column(DateTime)
