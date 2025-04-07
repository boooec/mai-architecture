import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import asyncio
from app.auth import get_password_hash
from app.db import async_session_maker
from app.models import User
from sqlalchemy import select


async def create_admin():
    async with async_session_maker() as session:
        result = await session.execute(select(User).where(User.login == "admin"))
        user = result.scalar_one_or_none()

        if user:
            print("Admin already exists")
            return

        admin = User(
            full_name="Administrator",
            login="admin",
            hashed_password=get_password_hash("secret"),
        )
        session.add(admin)
        await session.commit()
        print("Admin user created")


if __name__ == "__main__":
    asyncio.run(create_admin())
