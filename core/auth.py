import datetime
import jwt
import os

jwt_secret = os.getenv("JWT_SECRET", "1145141919810")
jwt_change = datetime.timedelta(days=30)


def create_access_token(username: str, password: str):
    pass

