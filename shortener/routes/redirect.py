import logging

from fastapi import APIRouter, HTTPException, Response
from sqlalchemy.exc import NoResultFound
from sqlmodel import select

from shortener import b62, models
from shortener.db import SessionDep

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/{shortened}")
def redirect(shortened: str, session: SessionDep, response: Response):
    """Return the shortened url in the Location header with a 302 HTTP response.

    :param shortened: the shortened url that is received from the HTTP route format.
    :param session: FastAPI dependency used to connect to the database.
    :param response: response object to modify. Will be sent back to client.
    """
    # Decode the passed in url route from base62 into a decimal integer.
    decoded_shortened = b62.decode(shortened)

    try:
        # Decimal integer will match primary id of link.
        link = session.exec(
            select(models.Link.original).where(models.Link.id == decoded_shortened)
        ).one()
    except NoResultFound:
        raise HTTPException(status_code=404)

    response.status_code = 302
    response.headers["Location"] = link
