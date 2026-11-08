from datetime import datetime
from pydantic import BaseModel, HttpUrl

class LinkCreate(BaseModel):
    url: HttpUrl

class LinkOut(BaseModel):
    id: int
    url: str
    hits: int
    created_at: datetime
