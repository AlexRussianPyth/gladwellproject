from uuid import uuid4
import datetime as dt

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4)
    email = Column(String(100), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    goals_achieved = Column(Integer, default=0)
    register_date = Column(Date)
    goals = relationship("Goal", back_populates="users")


class Goal(Base):
    __tablename__ = "goals"

    goal_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    name = Column(String(100), nullable=False)
    description = Column(String(250))
    created_at = Column(DateTime(), default=dt.datetime.now)
    updated_at = Column(
        DateTime(),
        default=dt.datetime.now,
        onupdate=dt.datetime.now)
    expired_at = Column(DateTime(), nullable=True)
    users = relationship("User", back_populates="goals")
    timeunits = relationship("Timeunit")


class Timeunit(Base):
    __tablename__ = "timeunits"

    timeunit_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4)
    goal_id = Column(UUID(as_uuid=True), ForeignKey("goals.goal_id"))
    info = Column(String(100), nullable=True)
    start_time = Column(DateTime(), nullable=True)
    end_time = Column(DateTime(), nullable=True)
