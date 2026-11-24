import os
from cryptography.fernet import Fernet

os.environ.setdefault("DROP_KEY", Fernet.generate_key().decode())

import pytest
from fastapi.testclient import TestClient
from src.db import get_connection, init_db
from src.main import app

@pytest.fixture
def db():
    init_db()
    with get_connection() as conn:
        conn.execute("TRUNCATE drops")

@pytest.fixture
def client(db):
    return TestClient(app)
