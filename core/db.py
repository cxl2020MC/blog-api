from motor import motor_asyncio
import os

db_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")

_client = motor_asyncio.AsyncIOMotorClient(db_url)
db = _client["blog_nuxt"]

users = db["users"]
posts = db["posts"]
# comments = db["comments"]
