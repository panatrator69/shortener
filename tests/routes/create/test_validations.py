"""Tests the validations on the POST /app/create endpoint."""

from sqlmodel import col, func, select

from shortener import b62
from shortener.models import Link


def test_empty_url(test_client, session):
    resp = test_client.post("/app/create", json={"url": ""})
    body = resp.json()

    assert resp.status_code == 422
    assert len(body["detail"]) == 1
    assert body["detail"][0]["ctx"]["error"] == "input is empty"

    assert session.exec(select(func.count(col(Link.id)))).one() == 0


def test_invalid_url(test_client, session):
    resp = test_client.post("/app/create", json={"url": "asdasdasd"})
    body = resp.json()

    assert resp.status_code == 422
    assert len(body["detail"]) == 1
    assert body["detail"][0]["ctx"]["error"] == "relative URL without a base"

    assert session.exec(select(func.count(col(Link.id)))).one() == 0


def test_ftp_url(test_client, session):
    resp = test_client.post(
        "/app/create", json={"url": "ftp://dropbox.com/or/something"}
    )
    body = resp.json()

    assert resp.status_code == 422
    assert len(body["detail"]) == 1
    assert body["detail"][0]["ctx"]["expected_schemes"] == "'http' or 'https'"

    assert session.exec(select(func.count(col(Link.id)))).one() == 0


def test_nonexistent_link(test_client, session):
    link = Link(original="http://youtube.com/", shortened="1")
    session.add(link)
    session.commit()

    nonexistent_shortened = b62.encode(654321)
    resp = test_client.get(f"/{nonexistent_shortened}", follow_redirects=False)

    assert resp.status_code == 404
