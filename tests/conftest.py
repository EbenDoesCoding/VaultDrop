import pytest
from src.db import get_connection, init_db
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def db():
    init_db()
    with get_connection() as conn:
        conn.execute("TRUNCATE links RESTART IDENTITY")

@pytest.fixture
def client(db):
	return TestClient(app)
