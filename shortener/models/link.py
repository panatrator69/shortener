"""Relates a given link to a shortened link."""

from datetime import datetime, timezone

from sqlmodel import SQLModel, Field


class Link(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    original: str = Field()
    shortened: str = Field()
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
