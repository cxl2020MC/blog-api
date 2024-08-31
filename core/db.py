from motor import motor_asyncio
import os

# 狗屎vercel的事件循环好像一个请求新建一个新的 这样写不行（
'''
db_url = os.getenv("MONGODB_URI", "mongodb://localhost:27017")

_client = motor_asyncio.AsyncIOMotorClient(db_url)
db = _client["blog_nuxt"]

users = db["users"]
posts = db["posts"]
'''
# 这个理论上会炸内存
'''
def get_db():
  db_url = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
  _client = motor_asyncio.AsyncIOMotorClient(db_url)
  db = _client["blog_nuxt"]
  return db
'''

# 拿class写个用with自动销毁连接的
class DB:
  def __init__(self, db_uri: str = os.getenv("MONGODB_URI", "mongodb://localhost:27017")):
    self.db_uri = db_uri
  async def __aenter__(self):
    self._client = motor_asyncio.AsyncIOMotorClient(self.db_uri)
    self.db = self._client["blog_nuxt"]
    print("创建数据库连接")
    return self

  async def __aexit__(self, exc_type, exc, tb):
    self._client.close()
    print("数据库连接已关闭")
  
  
  
