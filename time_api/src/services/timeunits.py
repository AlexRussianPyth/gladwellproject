import uuid

from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from src.db.sql_alchemy import get_engine, get_session
from src.models import models, dataclasses


class TimeunitsService:
    """Works with Timeunits in database"""
    def __init__(self):
        self.engine = get_engine()

    async def get_all(self) -> list[dataclasses.Timeunit]:
        """Return all Timeunits in database"""
        async with get_session(self.engine) as session:
            result = await session.execute(select(models.Timeunit))
            all_timeunits = result.scalars().all()

            return [dataclasses.Timeunit(**timeunit.__dict__) for timeunit in all_timeunits]

    async def get_timeunit_by_id(self, timeunit_id: uuid.UUID) -> dataclasses.Timeunit | None:
        """Return Timeunit from database"""
        async with get_session(self.engine) as session:
            result = await session.execute(select(models.Timeunit).where(models.Timeunit.timeunit_id == timeunit_id))
            timeunit = result.scalars().all()
            if not timeunit:
                return None
            return dataclasses.Timeunit(**timeunit[0].__dict__)

    async def add_timeunit(self, data: dataclasses.Timeunit) -> dataclasses.Timeunit | None:
        """
        Add new timeunit to database.

        Returns:
        Created timeunit if creation is successful
        None if timeunit is not found
        """
        async with get_session(self.engine) as session:
            timeunit_data = {
                "timeunit_id": uuid.uuid4(),
                "goal_id": data.goal_id,
                "info": data.info,
                "start_time": data.start_time,
                "end_time": data.end_time
            }
            timeunit = models.Timeunit(**timeunit_data)
            try:
                session.add(timeunit)
                await session.commit()
            except IntegrityError:
                await session.rollback()
                return None
            return dataclasses.Timeunit(**timeunit_data)

    async def update_timeunit(self, timeunit_id: uuid.UUID, data: dataclasses.TimeunitPatchIn) -> bool:
        """ Updates existing timeunit """
        async with get_session(self.engine) as session:
            result = await session.execute(select(models.Timeunit).where(models.Timeunit.timeunit_id == timeunit_id))
            timeunit = result.scalars().one()

            # TODO Rewrite without such strong coupling
            timeunit.info = data.info if not None else timeunit.info
            timeunit.start_time = data.start_time if not None else timeunit.start_time
            timeunit.end_time = data.end_time if not None else timeunit.end_time

            await session.commit()

            return True

    async def delete_timeunit(self, timeunit_id: uuid.UUID) -> dataclasses.Timeunit | None:
        """ Delete timeunit from database """
        async with get_session(self.engine) as session:
            result = await session.execute(select(models.Timeunit).where(models.Timeunit.timeunit_id == timeunit_id))
            timeunit = result.scalars().all()
            if not timeunit:
                return None
            await session.delete(timeunit[0])
            await session.commit()

            return dataclasses.Timeunit(**timeunit[0].__dict__)
