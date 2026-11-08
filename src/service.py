from src.db import get_connection

def _to_dict(row):
    return {"id": row[0], "url": row[1], "hits": row[2], "created_at": row[3]}

def create_link(url: str) -> dict:
    with get_connection() as conn:
        row = conn.execute(
            "INSERT INTO links (url) VALUES (%s) RETURNING id, url, hits, created_at",
            (url,),
        ).fetchone()
    return _to_dict(row)

def resolve_link(link_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            "UPDATE links SET hits = hits + 1 WHERE id = %s "
            "RETURNING id, url, hits, created_at",
            (link_id,),
        ).fetchone()
    return _to_dict(row) if row else None

def list_links() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, url, hits, created_at FROM links ORDER BY id"
        ).fetchall()
    return [_to_dict(r) for r in rows]

def get_stats(link_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT id, url, hits FROM links WHERE id = %s", (link_id,)
        ).fetchone()
    return {"id": row[0], "url": row[1], "hits": row[2]} if row else None
