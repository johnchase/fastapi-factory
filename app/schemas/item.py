from typing import Optional

from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    """ItemBase."""

    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class ItemCreate(ItemBase):
    """ItemCreate."""

    title: str


# Properties to receive on item update
class ItemUpdate(ItemBase):
    """ItemUpdate."""

    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    """ItemInDBBase."""

    id: int
    title: str
    owner_id: int

    class Config:
        """Config."""

        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    """Item."""

    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    """ItemInDB."""

    pass
