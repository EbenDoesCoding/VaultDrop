def test_list_empty(client):
    r = client.get("/links")
    assert r.status_code == 200
    assert r.json() == []


def test_list_returns_created_links(client):
    client.post("/links", json={"url": "https://example.com/a"})
    client.post("/links", json={"url": "https://example.com/b"})
    urls = [link["url"] for link in client.get("/links").json()]
    assert urls == ["https://example.com/a", "https://example.com/b"]


def test_stats_does_not_count_a_hit(client):
    link = client.post("/links", json={"url": "https://example.com/a"}).json()
    client.get(f"/links/{link['id']}")
    client.get(f"/links/{link['id']}")
    first = client.get(f"/links/{link['id']}/stats")
    second = client.get(f"/links/{link['id']}/stats")
    assert first.json()["hits"] == 2
    assert second.json()["hits"] == 2


def test_stats_unknown_id_returns_404(client):
    assert client.get("/links/9999/stats").status_code == 404


def test_stats_bad_id_returns_400(client):
    assert client.get("/links/abc/stats").status_code == 400
