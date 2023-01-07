import datetime as dt
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    user_id: UUID | None
    email: str | None
    name: str | None
    goals_achieved: int | None
    register_date: dt.date | None


class UserIn(BaseModel):
    """Model for registering new User"""
    email: str
    name: str
    register_date: dt.date = dt.date.today()


class Goal(BaseModel):
    goal_id: UUID
    user_id: UUID
    name: str
    description: str
    created_at: dt.datetime
    updated_at: dt.datetime
    expired_at: dt.datetime


class GoalIn(BaseModel):
    """Model for adding new Goal"""
    user_id: UUID
    name: str
    description: str
    created_at: dt.datetime = dt.datetime.now()
    expired_at: dt.datetime


class Timeunit(BaseModel):
    timeunit_id: UUID
    goal_id: UUID
    info: str
    start_time: dt.datetime
    end_time: dt.datetime
