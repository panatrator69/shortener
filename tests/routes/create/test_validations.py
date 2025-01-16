"""Tests the validations on the POST /app/create endpoint."""

from shortener.models import Link
from shortener import b62

from sqlmodel import col, func, select


def test_empty_url(test_client, session):
    resp = test_client.post("/app/create", json={"url": ""})

    assert resp.status_code == 400
    assert resp.json()["detail"] == "URL cannot be empty"

    assert session.exec(select(func.count(col(Link.id)))).one() == 0


def test_nonexistent_link(test_client, session):
    link = Link(original="http://youtube.com", shortened="1")
    session.add(link)
    session.commit()

    nonexistent_shortened = b62.encode(654321)
    resp = test_client.get(f"/{nonexistent_shortened}", follow_redirects=False)

    assert resp.status_code == 404
