from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_items() -> Any:
    """
    Retrieve items
    """
    return "Hello World"
