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

    async def get_goal_by_id(self, goal_id: uuid.UUID) -> dataclasses.Goal | None:
        """Return Goal from database"""
        async with get_session(self.engine) as session:
            result = await session.execute(select(models.Goal).where(models.Goal.goal_id == goal_id))
            goal = result.scalars().all()
            if not goal:
                return None
            return dataclasses.Goal(**goal[0].__dict__)

    async def get_timeunits_by_goal_id(self, goal_id: uuid.UUID) -> list[dataclasses.Timeunit]:
        """Return Timeunits by Goal from database"""
        async with get_session(self.engine) as session:
            result = await session.execute(select(models.Timeunit).where(models.Timeunit.goal_id == goal_id))
            all_timeunits = result.scalars().all()

            return [dataclasses.Timeunit(**timeunit.__dict__) for timeunit in all_timeunits]

    async def add_goal(self, data: dataclasses.GoalIn) -> dataclasses.Goal | None:
        """
        Add new Goal to database.

        Returns:
        Created goal if creation is successful
        None if goal is not found
        """
        async with get_session(self.engine) as session:
            goal_data = {
                "goal_id": uuid.uuid4(),
                "user_id": data.user_id,
                "name": data.name,
                "description": data.description,
                "created_at": data.created_at,
                "updated_at": data.created_at,
                "expired_at": data.expired_at,
            }
            goal = models.Goal(**goal_data)
            try:
                session.add(goal)
                await session.commit()
            except IntegrityError:
                await session.rollback()
                return None
            return dataclasses.Goal(**goal_data)

    async def update_goal(self, goal_id: uuid.UUID, data: dataclasses.GoalPatchIn) -> bool:
        """ Updates existing Goal """
        async with get_session(self.engine) as session:
            result = await session.execute(select(models.Goal).where(models.Goal.goal_id == goal_id))
            goal = result.scalars().one()

            # TODO Rewrite without such strong coupling
            goal.description = data.description if not None else goal.description
            goal.name = data.name if not None else goal.name
            goal.expired_at = data.expired_at if not None else goal.expired_at

            await session.commit()

            return True

    async def delete_goal(self, goal_id: uuid.UUID) -> dataclasses.Goal | None:
        """ Delete Goal from database """
        async with get_session(self.engine) as session:
            result = await session.execute(select(models.Goal).where(models.Goal.goal_id == goal_id))
            goal = result.scalars().all()
            if not goal:
                return None
            await session.delete(goal[0])
            await session.commit()

            return dataclasses.Goal(**goal[0].__dict__)
