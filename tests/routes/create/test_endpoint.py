"""Tests for a successful execution on the POST /app/create endpoint."""
from shortener.models import Link

from sqlmodel import col, func, select


def test_empty_url(test_client, session):
    resp = test_client.post('/app/create', json={'url': 'http://youtube.com'})

    assert resp.status_code == 201
    assert resp.json() == {
        'original': 'http://youtube.com',
        'shortened': 'test',
    }

    assert session.exec(select(func.count(col(Link.id)))).one() == 1

