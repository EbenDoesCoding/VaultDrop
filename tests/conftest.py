import os

import pytest
<<<<<<< HEAD
=======
from cryptography.fernet import Fernet
>>>>>>> origin/main
from fastapi.testclient import TestClient
from psycopg.conninfo import conninfo_to_dict

import src.db as database
from src.main import app


@pytest.fixture
def db(monkeypatch):
    test_url = os.environ.get("TEST_DATABASE_URL")
    if not test_url:
        pytest.fail("Set TEST_DATABASE_URL to the dedicated vaultdrop_test database.")

    if conninfo_to_dict(test_url).get("dbname") != "vaultdrop_test":
        pytest.fail("TEST_DATABASE_URL must point to a database named vaultdrop_test.")

    monkeypatch.setattr(database, "DATABASE_URL", test_url)
    database.init_db()
    with database.get_connection() as conn:
        conn.execute("TRUNCATE drops")



@pytest.fixture
<<<<<<< HEAD
def client(db):
=======
def client(db, monkeypatch):
    monkeypatch.setenv("DROP_KEY", Fernet.generate_key().decode("ascii"))
>>>>>>> origin/main
    return TestClient(app)
