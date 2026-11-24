from typing import Annotated

from fastapi import APIRouter, HTTPException, Path

from src import service
from src.models import LinkCreate, LinkOut, LinkStats
from src import service
from src.models import DropCreate, DropCreated, DropOut

Token = Annotated[str, Path(min_length=20, max_length=100)]

router = APIRouter(prefix="/drops")


@router.post("", response_model=LinkOut, status_code=201)
def create_link(body: LinkCreate):
    return service.create_link(str(body.url))


@router.get("/{link_id}", response_model=LinkOut)
def resolve_link(link_id: LinkId):
    link = service.resolve_link(link_id)
    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return link


@router.get("", response_model=list[LinkOut])
def list_links():
    return service.list_links()


@router.get("/{link_id}/stats", response_model=LinkStats)
def link_stats(link_id: LinkId):
    stats = service.get_stats(link_id)
    if stats is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return stats
@router.post("", response_model=DropCreated, status_code=201)
def create_drop(body: DropCreate, response: Response):
    response.headers["Cache-Control"] = "no-store"
    token = service.create_drop(body.secret, body.max_views, body.ttl_seconds)
    return {"token": token}

@router.get("/{token}", response_model=DropOut)
def open_drop(token: Token, response: Response):
    response.headers["Cache-Control"] = "no-store"
    try:
        return {"secret": service.consume_drop(token)}
    except service.DropNotFound:
        raise HTTPException(status_code=404, detail="Drop not found")
    except service.DropGone:
        raise HTTPException(status_code=410, detail="Drop expired or already used")
