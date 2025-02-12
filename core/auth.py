from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import datetime
import jwt
from jwt.exceptions import InvalidTokenError
import os
import json


jwt_secret = os.getenv("JWT_SECRET", "1145141919810")
jwt_change = datetime.timedelta(days=30)

if jwt_secret == "1145141919810":
    print("警告: JWT_SECRET环境变量未设置!")

user_db = os.getenv("USER_DB", '[{"username": "admin", "password": "114514"}]')

user_db = json.loads(user_db)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(username: str, password: str) -> str:
    data = {"username": username, "password": password,
            "exp": datetime.datetime.now(datetime.UTC) + jwt_change}
    token = jwt.encode(data, jwt_secret, algorithm="HS256")
    return token


def get_data_from_token(token: str = Depends(oauth2_scheme)):
    try:
        data = jwt.decode(token, jwt_secret, algorithms=["HS256"])
        return data
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Token 无效，请重新登陆", headers={"WWW-Authenticate": "Bearer"})


def verify_user(username: str, password: str) -> bool:
    if {"username": username, "password": password} in user_db:
        return True