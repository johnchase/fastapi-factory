from sqlalchemy import Column, String, ForeignKey, Integer
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID


class Ingredients(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    recipe_id = Column(UUID, ForeignKey("recipe.id"))
    step = Column(Integer)
    instruction = Column(String)
