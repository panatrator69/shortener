"""Stores environment variables within the shortener.settings.settings object."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_uri: str


# Import this object. Not the class.
settings = Settings()
