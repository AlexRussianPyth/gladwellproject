import uuid

from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from src.db.sql_alchemy import get_engine, get_session
from src.models import models, dataclasses


class UserService:
    """Works with Users in database"""

    async def get_all(self) -> list[dataclasses.User]:
        """Return all Users in database"""
        async with get_session(get_engine()) as session:
            result = await session.execute(select(models.User))
            all_users = result.scalars().all()

            return [dataclasses.User(**user.__dict__) for user in all_users]

    async def add_user(self, data: dataclasses.UserIn) -> bool:
        """Add new User to database. Returns True if creation is successful"""
        async with get_session(get_engine()) as session:
            user = models.User(
                user_id=uuid.uuid4(),
                email=data.email,
                goals_achieved=0,
                name=data.name,
                register_date=data.register_date
            )

            try:
                session.add(user)
                await session.commit()
            except IntegrityError:
                return False

            return True
