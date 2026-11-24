from fastapi import APIRouter, HTTPException, Path
from src import service
from src.models import LinkCreate, LinkOut, LinkStats
from typing import Annotated

LinkId = Annotated[int, Path(ge=1, le=2_147_483_647)]

router = APIRouter(prefix="/links")

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
