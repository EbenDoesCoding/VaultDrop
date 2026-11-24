from fastapi.testclient import TestClient

from src.main import app


def test_landing_page():
    response = TestClient(app).get("/")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "<title>VaultDrop</title>" in response.text
    assert 'href="/style.css"' in response.text
    assert "<fieldset disabled>" in response.text


def test_stylesheet():
    response = TestClient(app).get("/style.css")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/css")


def test_frontend_keeps_api_routes_reachable():
    client = TestClient(app)

    assert client.get("/health").json() == {"status": "ok"}
    assert client.post("/drops", json={}).status_code == 400
    assert client.get("/drops/too-short").status_code == 400


def test_missing_asset():
    assert TestClient(app).get("/missing.css").status_code == 404
