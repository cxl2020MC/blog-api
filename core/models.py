from pydantic import BaseModel

class User(BaseModel):
    _id: str | None = None
    name: str
    email: str
    hashed_password: str

class Post(BaseModel):
    _id: str | None = None
    title: str
    abbrlink: str
    author: str
    content: str
    tags: list[str]
    created_at: float
    updated_at: float
    draft: bool = False
    word_count: int
