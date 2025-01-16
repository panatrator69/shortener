"""Tests for a successful execution on the POST /app/create endpoint."""

from sqlmodel import col, func, select

from shortener.models import Link


def test_successful_shortening(test_client, session):
    resp = test_client.post("/app/create", json={"url": "http://youtube.com/"})
    body = resp.json()

    assert resp.status_code == 201
    assert body.pop("created_at") is not None
    assert body == {
        "original": "http://youtube.com/",
        "shortened": "1",
    }

    assert session.exec(select(func.count(col(Link.id)))).one() == 1

    resp = test_client.get(f"/{resp.json()['shortened']}", follow_redirects=False)
    assert resp.status_code == 302
    assert resp.headers["Location"] == "http://youtube.com/"


def test_shortening_existing(test_client, session):
    """Test that the API returns an HTTP 200 whenever an existing link in the system is shortened again."""
    test_successful_shortening(test_client, session)
    resp = test_client.post("/app/create", json={"url": "http://youtube.com/"})
    body = resp.json()

    assert resp.status_code == 200
    assert body.pop("created_at") is not None
    assert body == {
        "original": "http://youtube.com/",
        "shortened": "1",
    }

    assert session.exec(select(func.count(col(Link.id)))).one() == 1

    resp = test_client.get(f"/{resp.json()['shortened']}", follow_redirects=False)
    assert resp.status_code == 302
    assert resp.headers["Location"] == "http://youtube.com/"
