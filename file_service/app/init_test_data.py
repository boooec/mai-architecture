import asyncio
import os
import random
import string
import base64
from datetime import datetime

from faker import Faker
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv("MONGODB_URL", "mongodb://mongo_db:27017")
DB_NAME = os.getenv("MONGODB_DB", "files_db")

NUM_FILES = 100
FILENAME_LEN = 15
FILE_SIZE = 100_000

fake = Faker()


async def init_dummy_routes():
    client = AsyncIOMotorClient(MONGO_URL)
    col = client[DB_NAME].files

    count = await col.count_documents({})
    if count >= NUM_FILES:
        client.close()
        return

    files = []
    for i in range(NUM_FILES):
        folder_id = random.randint(1, 3)
        filename = ''.join(random.choices(string.ascii_letters + string.digits, k=FILENAME_LEN))
        content = base64.b64encode(random.randbytes(FILE_SIZE)).decode("utf-8")
        files.append({"folder_id": folder_id, "filename": filename, "content": content, "created_at": datetime.now()})

    _ = await col.insert_many(files)
    client.close()


if __name__ == "__main__":
    asyncio.run(init_dummy_routes())
