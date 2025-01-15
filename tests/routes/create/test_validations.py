"""Tests the validations on the POST /app/create endpoint."""
from shortener.models import Link

from sqlmodel import col, func, select


def test_empty_url(test_client, session):
    resp = test_client.post('/app/create', json={'url': ''})

    assert resp.status_code == 400
    assert resp.json()['detail'] == 'URL cannot be empty'

    assert session.exec(select(func.count(col(Link.id)))).one() == 0

