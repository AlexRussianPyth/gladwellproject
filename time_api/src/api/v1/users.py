from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate

from src.models import dataclasses
from src.services.users import UserService


router = APIRouter()


@router.get(
    "/",
    response_model=Page[dataclasses.User],
    summary="Get All Users",
    status_code=HTTPStatus.OK,
    tags=["users"],
    response_description="All Registered Users in Database")
async def get_all_users(users_service: UserService = Depends()):
    """Return all Users in database"""
    users = await users_service.get_all()
    return paginate(users)


@router.get("/{user_id}", response_model=dataclasses.User, summary="Get User by ID",
            status_code=HTTPStatus.OK, tags=["users"], response_description="User by concrete id")
async def get_user_by_id(user_id: UUID, users_service: UserService = Depends()):
    """Return Single User by id"""
    user = await users_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    return user


@router.post("/", summary="Add New User", status_code=HTTPStatus.CREATED, tags=["users"])
async def add_user(data: dataclasses.UserIn, users_service: UserService = Depends()):
    user = await users_service.add_user(data)
    if not user:
        raise HTTPException(status_code=400, detail="User with such data already created")
    return user


@router.patch("/{user_id}", summary="Update User", status_code=HTTPStatus.NO_CONTENT, tags=["users"])
async def update_user(user_id: UUID, data: dataclasses.User, users_service: UserService = Depends()):
    user = await users_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    print(f"DATA!{data}")
    await users_service.update_user(user_id, data)
    return {"msg": "Updating Successful"}


@router.delete("/{user_id}", summary="Delete User", status_code=HTTPStatus.OK, tags=["users"])
async def delete_user(user_id: UUID, users_service: UserService = Depends()):
    user = await users_service.delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    return {"msg": "Success", "deleted_user": user}
