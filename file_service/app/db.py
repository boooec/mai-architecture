import asyncio
import os

from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://mongo_db:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "files_db")

client = AsyncIOMotorClient(MONGODB_URL)
db = client[MONGODB_DB]


async def ensure_indexes():
    col = db.files_db
    await col.create_index("file_id")
    await col.create_index("folder_id")
    await col.create_index("filename")
