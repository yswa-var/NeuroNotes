from pydantic import BaseModel
from typing import List, Optional

class Flashcard(BaseModel):
    id: Optional[str] = None
    topic: str
    question: str
    answer: str
    difficulty: int = 1
    tags: List[str] = []
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class Hello(BaseModel):
    message: str

class Lms(BaseModel):
    response: str