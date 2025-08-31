from pydantic import BaseModel


class Response[T](BaseModel):
    code: int = 200
    msg: str = "Success"
    data: T | None = None


class User(BaseModel):
    username: str
    password: str

class Post(BaseModel):
    _id: str | None = None
    title: str
    link: str
    cover: str
    author: str
    md_content: str | None = None
    tags: list[str]
    created_at: float
    updated_at: float
    draft: bool = False
    word_count: int



class PostResponse(Response[list[Post]]):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str