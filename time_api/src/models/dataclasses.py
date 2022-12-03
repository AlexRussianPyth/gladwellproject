from uuid import UUID
import datetime as dt

from pydantic import BaseModel


class User(BaseModel):
    user_id: UUID
    email: str
    name: str
    goals_achieved: int
    register_date: dt.datetime


class Goal(BaseModel):
    goal_id: UUID
    user_id: UUID
    name: str
    description: str
    created_at: dt.datetime
    updated_at: dt.datetime
    expired_at: dt.datetime


class Timeunit(BaseModel):
    timeunit_id: UUID
    goal_id: UUID
    info: str
    start_time: dt.datetime
    end_time: dt.datetime


