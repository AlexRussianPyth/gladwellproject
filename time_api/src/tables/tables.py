import uuid
import datetime as dt

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.dialects.postgresql import UUID

from src.db.sql_alchemy import Base


class Goals(Base):
    __tablename__ = "goals"  # Обязательный параметр-название таблицы

    goal_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    description1 = Column(String(250))
    created_at = Column(DateTime(), default=dt.now)
    updated_at = Column(DateTime(), default=dt.now, onupdate=dt.now)
    expired_at = Column(DateTime(), nullable=True)
    duration = Column(Integer, nullable=True)
