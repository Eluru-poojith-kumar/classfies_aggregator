
from pydantic import BaseModel
from typing import List, Optional

class Classified(BaseModel):
    title: str
    description: str
    category: str
    location: str
    language: str
    posted_by: str
    tags: Optional[List[str]] = []

class User(BaseModel):
    user_id: str
    preferences: Optional[List[str]] = []
