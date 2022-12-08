from fastapi import APIRouter
from sqlalchemy.future import select

from src.db.sql_alchemy import get_engine, get_session
from src.models import models, dataclasses

router = APIRouter()


@router.get("/", response_model=list[dataclasses.User], summary="Get All Users")
async def get_all_users():
    """Return all Users in database"""
    async with get_session(get_engine()) as session:
        result = await session.execute(select(models.User))
        all_users = result.scalars().all()

        return [dataclasses.User(**user.__dict__) for user in all_users]