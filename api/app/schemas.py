from pydantic import BaseModel, HttpUrl
from typing import Optional, List

class ItemCreate(BaseModel):
    url: HttpUrl
    title: Optional[str] = None
    thumbnail_url: Optional[str] = None
    notes: Optional[str] = None
    rank: int = 0

class ItemRead(BaseModel):
    id: int
    url: str
    title: Optional[str]
    thumbnail_url: Optional[str]
    notes: Optional[str]
    rank: int
    class Config: from_attributes = True
