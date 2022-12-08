from fastapi import APIRouter
from sqlalchemy.future import select
import json

from src.db.sql_alchemy import get_engine, get_session
from src.models import models, dataclasses

router = APIRouter()


@router.get("/", summary="Get All Users")
async def get_all_users():
    """Return all Users in database"""
    engine = get_engine()
    async with get_session(engine) as session:
        stmt = select(models.User)
        result = await session.execute(stmt)
        all_users = result.scalars().all()
        await session.commit()
        print([user.__dict__ for user in all_users])
    # return [dataclasses.User(**user.__dict__) for user in all_users]
    return 
