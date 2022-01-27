"""Base settings for test class."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

TEST_URL = str(settings.SQLALCHEMY_TEST_DATABASE_URI)
engine = create_engine(TEST_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """Override get_db to use testing database instead."""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()  # type: ignore
