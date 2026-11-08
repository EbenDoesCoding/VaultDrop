def test_resolve_counts_hits(client):
    link = client.post("/links", json={"url": "https://example.com/page"}).json()
    first = client.get(f"/links/{link['id']}")
    second = client.get(f"/links/{link['id']}")
    assert first.status_code == 200
    assert first.json()["hits"] == 1
    assert second.json()["hits"] == 2

def test_resolve_unknown_id_returns_404(client):
    assert client.get("/links/9999").status_code == 404

def test_resolve_bad_id_returns_400(client):
    assert client.get("/links/abc").status_code == 400
