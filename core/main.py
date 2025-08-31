from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from . import utils
from .db import DB
from . import models
from . import auth

router = APIRouter()


@router.get("/", response_model=models.Response)
async def root():
    return models.Response(msg="博客api正常运行")


@router.get("/posts")
async def 获取文章列表() -> models.PostResponse:
    async with DB() as db:
        data = await db.posts.find({}, {"md_content": 0}).to_list(length=100)

        data = utils.id_list_replace(data)
        print(data)
        return models.PostResponse(data=data)


@router.get("/posts/{link}", response_model=models.Response)
async def 获取文章内容(link: str):
    async with DB() as db:
        data = await db.posts.find_one({"link": link})
        if data is None:
            return models.Response(code=404, msg="文章不存在")
        data = utils.id_replace(data)
        return utils.return_data(data)


@router.post("/posts", response_model=models.Response)
async def 上传文章(data: models.Post, user=Depends(auth.get_data_from_token)):
    async with DB() as db:
        await db.posts.insert_one(dict(data))
        return utils.return_data(msg="上传成功")

@router.post("/user", response_model=models.Response)
async def 获取用户信息(data: models.Post, user=Depends(auth.get_data_from_token)):
    return utils.return_data(user)

@router.post("/token", response_model=models.Token)
async def login(from_data: OAuth2PasswordRequestForm = Depends()):
    if not auth.verify_user(from_data.username, from_data.password):
        raise HTTPException(status_code=400, detail="用户名或密码错误")
    token = auth.create_access_token(from_data.username, from_data.password)
    return models.Token(access_token=token, token_type="bearer")

# @router.get("/ip")
# async def get_ip():

#     return utils.return_data(msg="ip地址获取成功")