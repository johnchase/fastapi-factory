from sqlalchemy import Column, String, Float
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID


class Ingredients(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    name = Column(String)
    weight = Column(Float)
    volume = Column(Float)
    count = Column(Float)
    calories = Column(Float)
    fat = Column(Float)
    protein = Column(Float)
    carbohydrates = Column(Float)
