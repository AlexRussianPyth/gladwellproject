import uuid

from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from src.db.sql_alchemy import get_engine, get_session
from src.models import models, dataclasses


class UserService:
    """Works with Users in database"""
    def __init__(self):
        self.engine = get_engine()

    async def get_all(self) -> list[dataclasses.User]:
        """Return all Users in database"""
        async with get_session(self.engine) as session:
            result = await session.execute(select(models.User))
            all_users = result.scalars().all()

            return [dataclasses.User(**user.__dict__) for user in all_users]

    async def get_user_by_id(self, user_id: uuid.UUID) -> dataclasses.User | None:
        """Return user from database"""
        async with get_session(self.engine) as session:
            result = await session.execute(select(models.User).where(models.User.user_id == user_id))
            user = result.scalars().all()
            if not user:
                return None
            return dataclasses.User(**user[0].__dict__)

    async def add_user(self, data: dataclasses.UserIn) -> dataclasses.User | None:
        """Add new User to database. Returns True if creation is successful"""
        async with get_session(self.engine) as session:
            user_data = {
                "user_id": uuid.uuid4(),
                "email": data.email,
                "goals_achieved": 0,
                "name": data.name,
                "register_date": data.register_date
            }
            user = models.User(**user_data)
            try:
                session.add(user)
                await session.commit()
            except IntegrityError:
                return None
            return dataclasses.User(**user_data)
