import datetime as dt
from uuid import uuid4

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

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
    goals = relationship("Goal", back_populates="users", cascade='save-update, merge, delete', passive_deletes=True)


class Goal(Base):
    __tablename__ = "goals"

    goal_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id", ondelete="CASCADE"))
    name = Column(String(100), nullable=False)
    description = Column(String(250))
    created_at = Column(DateTime(), default=dt.datetime.now)
    updated_at = Column(
        DateTime(),
        default=dt.datetime.now,
        onupdate=dt.datetime.now)
    expired_at = Column(DateTime(), nullable=True)
    users = relationship("User", back_populates="goals")
    timeunits = relationship("Timeunit", cascade='save-update, merge, delete', passive_deletes=True)


class Timeunit(Base):
    __tablename__ = "timeunits"

    timeunit_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4)
    goal_id = Column(UUID(as_uuid=True), ForeignKey("goals.goal_id", ondelete="CASCADE"))
    info = Column(String(100), nullable=True)
    start_time = Column(DateTime(), nullable=True)
    end_time = Column(DateTime(), nullable=True)
