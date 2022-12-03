import asyncio
import datetime as dt
import random
from collections import defaultdict
from uuid import UUID, uuid4

from faker import Faker
from src.core.config import settings
from src.db.sql_alchemy import get_engine, get_session
from src.models import dataclasses, models


class FakeDataGenerator:
    """Creates fake data for our project"""
    def __init__(self, num_users: int = 40, max_goals_per_user: int = 5, max_timeunits_per_goal: int = 20):
        self.num_users = num_users
        self.max_goals_per_user = max_goals_per_user
        self.max_timeunits_per_goal = max_timeunits_per_goal
        self.faker = Faker()

    def create_user_history(self) -> dict:
        """Creates connected user history"""
        history = defaultdict(list)
        for _ in range(self.num_users):
            user_id = uuid4()
            history["Users"].append(self._create_fake_user(user_id))

            for _ in range(random.randint(0, self.max_goals_per_user)):
                goal = self._create_fake_goal(user_id)
                history["Goals"].append(goal)

                for _ in range(random.randint(0, self.max_timeunits_per_goal)):
                    history["Timeunits"].append(self._create_fake_timeunit(goal.goal_id))

        return history

    def _create_fake_user(self, user_id: UUID) -> dataclasses.User:
        """Creates test data for single User"""
        user_fake_data = self.faker.simple_profile(sex=random.choice(("M", "F")))
        return dataclasses.User(user_id=user_id, email=user_fake_data["mail"],
                                name=user_fake_data["name"], goals_achieved=0,
                                register_date=self.faker.date_time())

    def _create_fake_goal(self, user_id: UUID) -> dataclasses.Goal:
        """Creates test data for single Goal"""
        return dataclasses.Goal(goal_id=uuid4(), user_id=user_id,
                                name=self.faker.name(),
                                description=self.faker.text(100),
                                created_at=self.faker.date_time(),
                                updated_at=self.faker.date_time(),
                                expired_at=self.faker.date_time())

    def _create_fake_timeunit(self, goal_id: UUID) -> dataclasses.Timeunit:
        """Creates test data for single Timeunit"""
        start_time = self.faker.date_time()
        end_time = start_time + dt.timedelta(hours=random.randint(1, 10), minutes=random.randint(0, 60))
        return dataclasses.Timeunit(timeunit_id=uuid4(), goal_id=goal_id, info=self.faker.text(20),
                                    start_time=start_time, end_time=end_time)


async def write_with_alchemy(test_data: dict) -> None:
    """Write fake data to alchemy tables"""
    # TODO Rewrite as generator
    engine = get_engine()
    async with get_session(engine) as session:
        users = []
        for user in test_data["Users"]:
            users.append(models.User(**user.dict()))

        goals = []
        for goal in test_data["Goals"]:
            goals.append(models.Goal(**goal.dict()))

        timeunits = []
        for timeunit in test_data["Timeunits"]:
            timeunits.append(models.Timeunit(**timeunit.dict()))

        session.add_all(users)
        await session.commit()

        session.add_all(goals)
        await session.commit()

        session.add_all(timeunits)
        await session.commit()


if __name__ == "__main__":
    fake_data_generator = FakeDataGenerator(
        settings.fakedata.num_users,
        settings.fakedata.max_goals_per_user,
        settings.fakedata.max_timeunits_per_goal)

    history = fake_data_generator.create_user_history()
    asyncio.run(write_with_alchemy(history))
