def test_empty_url(test_client):
    resp = test_client.post('/app/create', json={'url': ''})

    assert resp.status_code == 400
