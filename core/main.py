from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from . import utils
from .db import DB
from . import models
from . import auth

router = APIRouter()


@router.get("/", response_model=models.Response)
async def root():
    return utils.return_data(msg="博客api正常运行")


@router.get("/posts")
async def 获取文章列表():
    async with DB() as db:
        data = await db.posts.find({}, {"md_content": 0}).to_list(length=100)

        data = utils.id转换(data)
        print(data)
        return utils.return_data(data)


@router.get("/posts/{link}", response_model=models.Response)
async def 获取文章内容(link: str):
    async with DB() as db:
        data = await db.posts.find_one({"link": link})
        data["_id"] = str(data.get("_id"))
        return utils.return_data(data)


@router.post("/posts", response_model=models.Response)
async def 上传文章(data: models.Post):
    async with DB() as db:
        await db.posts.insert_one(dict(data))
        return utils.return_data(msg="上传成功")


@router.post("/token")
async def login(from_data: OAuth2PasswordRequestForm = Depends()):
    token = auth.create_access_token(from_data.username, from_data.password)
    return {"access_token": token}