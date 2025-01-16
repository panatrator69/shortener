import logging

from fastapi import HTTPException, APIRouter, Response
from sqlmodel import select
from sqlalchemy.exc import NoResultFound

from shortener import models
from shortener.db import SessionDep
from shortener import b62


logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/{shortened}")
def redirect(shortened: str, session: SessionDep, response: Response):
    """Return the shortened url in the Location header with a 302 HTTP response."""
    decoded_shortened = b62.decode(shortened)

    try:
        link = session.exec(
            select(models.Link.original).where(models.Link.id == decoded_shortened)
        ).one()
    except NoResultFound:
        raise HTTPException(status_code=404)

    response.status_code = 302
    response.headers["Location"] = link
