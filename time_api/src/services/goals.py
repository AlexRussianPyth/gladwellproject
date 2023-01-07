import uuid

from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from src.db.sql_alchemy import get_engine, get_session
from src.models import models, dataclasses


class GoalService:
    """Works with Goals in database"""
    def __init__(self):
        self.engine = get_engine()

    async def get_all(self) -> list[dataclasses.Goal]:
        """Return all Goals in database"""
        async with get_session(self.engine) as session:
            result = await session.execute(select(models.Goal))
            all_goals = result.scalars().all()

            return [dataclasses.Goal(**goal.__dict__) for goal in all_goals]
#
#     async def get_user_by_id(self, user_id: uuid.UUID) -> dataclasses.User | None:
#         """Return user from database"""
#         async with get_session(self.engine) as session:
#             result = await session.execute(select(models.User).where(models.User.user_id == user_id))
#             user = result.scalars().all()
#             if not user:
#                 return None
#             return dataclasses.User(**user[0].__dict__)
#
#     async def add_user(self, data: dataclasses.UserIn) -> dataclasses.User | None:
#         """
#         Add new User to database.
#
#         Returns:
#         Created User if creation is successful
#         None if user is not found
#         """
#         async with get_session(self.engine) as session:
#             user_data = {
#                 "user_id": uuid.uuid4(),
#                 "email": data.email,
#                 "goals_achieved": 0,
#                 "name": data.name,
#                 "register_date": data.register_date
#             }
#             user = models.User(**user_data)
#             try:
#                 session.add(user)
#                 await session.commit()
#             except IntegrityError:
#                 await session.rollback()
#                 return None
#             return dataclasses.User(**user_data)
#
#     async def update_user(self, user_id: uuid.UUID, data: dataclasses.User) -> bool:
#         """ updates existing User """
#         async with get_session(self.engine) as session:
#             result = await session.execute(select(models.User).where(models.User.user_id == user_id))
#             user = result.scalars().one()
#
#             # TODO Rewrite without such strong coupling
#             user.email = data.email if not None else user.email
#             user.name = data.name if not None else user.name
#             user.goals_achieved = data.goals_achieved if not None else user.goals_achieved
#             user.register_date = data.register_date if not None else user.register_date
#
#             await session.commit()
#
#             return True
#
#     async def delete_user(self, user_id: uuid.UUID) -> dataclasses.User | None:
#         """ Delete user from database """
#         async with get_session(self.engine) as session:
#             result = await session.execute(select(models.User).where(models.User.user_id == user_id))
#             user = result.scalars().all()
#             if not user:
#                 return None
#             await session.delete(user[0])
#             await session.commit()
#
#             return dataclasses.User(**user[0].__dict__)
#
