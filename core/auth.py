from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import datetime
import jwt
from jwt.exceptions import InvalidTokenError
import os

jwt_secret = os.getenv("JWT_SECRET", "1145141919810")
jwt_change = datetime.timedelta(days=30)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(username: str, password: str) -> str:
    data = {"username": username, "password": password,
            "exp": datetime.detetime.now(datetime.UTC) + jwt_change}
    token = jwt.encode(data, jwt_secret, algorithm="HS256")
    return token


def get_data_from_token(token: str = Depends(oauth2_scheme)):
    try:
        data = jwt.decode(token, jwt_secret, algorithms=["HS256"])
        return data
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token 无效，请重新登陆")

