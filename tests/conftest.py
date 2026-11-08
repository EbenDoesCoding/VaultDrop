import pytest
from src.db import get_connection, init_db

@pytest.fixture
def db():
    init_db()
    with get_connection() as conn:
        conn.execute("TRUNCATE links RESTART IDENTITY")
