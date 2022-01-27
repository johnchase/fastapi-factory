"""Dependencies module."""
from typing import Generator

from app.db.session import SessionLocal


def get_db() -> Generator:
    """Retrieve database from session."""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()  # type: ignore
