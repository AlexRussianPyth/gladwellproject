from fastapi import APIRouter, Depends

from src.models import dataclasses
from src.services.users import UserService, get_user_service


router = APIRouter()


@router.get("/", response_model=list[dataclasses.User], summary="Get All Users")
async def get_all_users(users_service: UserService = Depends(get_user_service)):
    """Return all Users in database"""
    users = await users_service.get_all()
    return users


@router.post("/", summary="Add New User")
async def add_user(data: dataclasses.UserIn, users_service: UserService = Depends(get_user_service)):
    """Add new User to database"""
    if await users_service.add_user(data):
        return {"msg": "Success"}
    return {"msg": "User is not created"}
