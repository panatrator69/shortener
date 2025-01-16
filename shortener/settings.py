"""Stores environment variables within the shortener.settings.settings object."""

from pydantic.networks import HttpUrl, PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_uri: PostgresDsn
    hostname: HttpUrl = "http://127.0.0.1:8000/"


# Import this object. Not the class.
settings = Settings()
