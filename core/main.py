from fastapi import APIRouter
from . import utils
from .db import DB
from . import models

router = APIRouter()

@router.get("/")
async def root():
    return utils.return_data(msg = "博客api正常运行")

@router.get("/posts")
async def 获取文章列表():
    async with DB() as db:
       data = await db.posts.find({}, {"md_content": 0}).to_list(length=100)
       data = utils.id转换(data)
       print(data)
       return utils.return_data(data)


@router.get("/posts/{link}")
async def 获取文章内容(link:str):
    async with DB() as db:
        data = await db.posts.find_one({"link": link})
        data = utils.id转换(data)
        return utils.return_data(data)

@router.post("/posts")
async def 上传文章(data: models.Post):
    async with DB() as db:
        await db.posts.insert_one(dict(data))
        return utils.return_data(msg = "上传成功")


