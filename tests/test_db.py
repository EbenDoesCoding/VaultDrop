from src.db import get_connection


def test_insert_and_read_link(db):
    with get_connection() as conn:
        row = conn.execute(
            "INSERT INTO links (url) VALUES (%s) RETURNING id, hits",
            ("https://example.com",),
        ).fetchone()
    assert row == (1, 0)
