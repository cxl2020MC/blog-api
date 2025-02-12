from pydantic import BaseModel


class Response(BaseModel):
    code: int = 200
    msg: str = "Success"
    data: dict | None = None

class User(BaseModel):
    _id: str | None = None
    name: str
    email: str
    hashed_password: str

class Post(BaseModel):
    _id: str | None = None
    title: str
    link: str
    cover: str
    author: str
    content: str
    tags: list[str]
    created_at: float
    updated_at: float
    draft: bool = False
    word_count: int


class Token(BaseModel):
    access_token: str
    token_type: str