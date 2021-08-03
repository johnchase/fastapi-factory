from sqlalchemy import Column, String, ForeignKey
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID


class RecipeIngredients(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    ingredient_id = Column(UUID, ForeignKey("ingredients.id"))
    recipe_id = Column(UUID, ForeignKey("recipe.id"))
    amount = Column(String)
