import os
import secrets
from typing import Any, Dict, List, Optional

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator, validate_model


class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    #     # 60 minutes * 24 hours * 8 days = 8 days
    #     ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    #     SERVER_NAME: str
    #     SERVER_HOST: AnyHttpUrl
    #     # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    #     # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    #     # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    #
    #     @validator("BACKEND_CORS_ORIGINS", pre=True)
    #     def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
    #         if isinstance(v, str) and not v.startswith("["):
    #             return [i.strip() for i in v.split(",")]
    #         elif isinstance(v, (list, str)):
    #             return v
    #         raise ValueError(v)
    #
    PROJECT_NAME: str = "FastAPI Factory"
    #     SENTRY_DSN: Optional[HttpUrl] = None
    #
    #     @validator("SENTRY_DSN", pre=True)
    #     def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
    #         if len(v) == 0:
    #             return None
    #         return v
    #
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_TEST_DB: str
    SQLALCHEMY_TEST_DATABASE_URI: Optional[PostgresDsn] = None
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    ENV_RUN_INITIAL_VALIDATION: bool = os.environ.get("RUN_INITIAL_VALIDATION", True)

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    @validator("SQLALCHEMY_TEST_DATABASE_URI", pre=True)
    def assemble_test_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        """assemble_test_db_connection.
        Parameters
        ----------
        v : Optional[str]
            v
        values : Dict[str, Any]
            values
        Returns
        -------
        Any
        """
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_TEST_DB') or ''}",
        )

    def check(self):
        """Run pydantic validation."""
        values, fields_set, validation_error = validate_model(self.__class__, self.__dict__)
        if validation_error:
            raise validation_error
        try:
            object.__setattr__(self, "__dict__", values)
        except TypeError as e:  # pragma: no cover
            raise TypeError(
                "Model values must be a dict; you may not have returned a dictionary from a root validator"
            ) from e
        object.__setattr__(self, "__fields_set__", fields_set)

    class Config:
        case_sensitive = True


settings = Settings.construct()
if settings.ENV_RUN_INITIAL_VALIDATION:
    settings.check()
