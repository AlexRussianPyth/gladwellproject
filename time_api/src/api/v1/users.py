from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from src.models import dataclasses
from src.services.users import UserService


router = APIRouter()


@router.get(
    "/",
    response_model=list[dataclasses.User],
    summary="Get All Users",
    status_code=HTTPStatus.OK,
    tags=["users"],
    response_description="All Registered Users in Database")
async def get_all_users(users_service: UserService = Depends()):
    """Return all Users in database"""
    users = await users_service.get_all()
    return users


@router.post("/", summary="Add New User", status_code=HTTPStatus.CREATED, tags=["users"])
async def add_user(data: dataclasses.UserIn, users_service: UserService = Depends()):
    """Add new User to database"""
    if not await users_service.add_user(data):
        raise HTTPException(status_code=400, detail="User is not created")
    return {"msg": "Success"}
