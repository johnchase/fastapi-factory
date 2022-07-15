from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    """CRUDItem."""

    def create_with_owner(self, db: Session, *, obj_in: ItemCreate, owner_id: int) -> Item:
        """create_with_owner.

        Parameters
        ----------
        db : Session
            db
        obj_in : ItemCreate
            obj_in
        owner_id : int
            owner_id

        Returns
        -------
        Item

        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100) -> List[Item]:
        """get_multi_by_owner.

        Parameters
        ----------
        db : Session
            db
        owner_id : int
            owner_id
        skip : int
            skip
        limit : int
            limit

        Returns
        -------
        List[Item]

        """
        return db.query(self.model).filter(Item.owner_id == owner_id).offset(skip).limit(limit).all()


item = CRUDItem(Item)
