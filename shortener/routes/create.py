import logging
from urllib.parse import urljoin

from fastapi import APIRouter, Response
from sqlmodel import select

from shortener import b62, dto, models
from shortener.db import SessionDep
from shortener.settings import settings

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/app/create")
def create(body: dto.Create, session: SessionDep, response: Response) -> dto.Link:
    url = body.url
    logger.debug(f"Received {url=}")

    existing_link = session.exec(
        select(models.Link).where(models.Link.original == str(url))
    ).one_or_none()

    if existing_link:
        response.status_code = 200
        return existing_link

    link = models.Link(original=str(url), shortened="")
    session.add(link)
    session.flush()
    session.refresh(link)

    # Join the hostname and path components of the new shortened URL together
    shortened_path = b62.encode(link.id)
    shortened = urljoin(str(settings.hostname), shortened_path)
    link.shortened = shortened

    session.commit()

    response.status_code = 201
    return link
