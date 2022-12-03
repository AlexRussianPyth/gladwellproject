import asyncio
from uuid import uuid4

from src.db.sql_alchemy import get_engine, get_session
from src.models.models import User


async def main():
    """Create test user"""
    engine = get_engine()
    async with get_session(engine) as session:
        user1 = User(
            user_id=uuid4(),
            email="alex@mail.ru",
            name="Alex",
            goals_achieved=0)
        session.add_all([user1])
        await session.commit()


if __name__ == "__main__":
    asyncio.run(main())
