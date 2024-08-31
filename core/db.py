from motor import motor_asyncio
import os

# 狗屎vercel的事件循环好像是一次性的 这样写不行（
'''
db_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")

_client = motor_asyncio.AsyncIOMotorClient(db_url)
db = _client["blog_nuxt"]

users = db["users"]
posts = db["posts"]
'''

def get_db():
  db_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
  _client = motor_asyncio.AsyncIOMotorClient(db_url)
  db = _client["blog_nuxt"]
  return db
