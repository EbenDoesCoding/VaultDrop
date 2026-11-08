def test_create_link(client):
    r = client.post("/links", json={"url": "https://example.com/page"})
    assert r.status_code == 201
    assert r.json()["url"] == "https://example.com/page"
    assert r.json()["hits"] == 0

def test_create_rejects_bad_url(client):
    assert client.post("/links", json={"url": "not-a-url"}).status_code == 400

def test_create_rejects_missing_url(client):
    assert client.post("/links", json={}).status_code == 400
