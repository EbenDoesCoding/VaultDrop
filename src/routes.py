from fastapi import APIRouter, HTTPException
from src import service
from src.models import LinkCreate, LinkOut

router = APIRouter(prefix="/links")

@router.post("", response_model=LinkOut, status_code=201)
def create_link(body: LinkCreate):
    return service.create_link(str(body.url))

@router.get("/{link_id}", response_model=LinkOut)
def resolve_link(link_id: int):
    link = service.resolve_link(link_id)
    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return link
