from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate

from src.models import dataclasses
from src.services.goals import GoalService


router = APIRouter()


@router.get(
    "/",
    response_model=Page[dataclasses.Goal],
    summary="Get All Goals",
    status_code=HTTPStatus.OK,
    tags=["goals"],
    response_description="All Goals in Database")
async def get_all_goals(goals_service: GoalService = Depends()):
    """Return all Goals in database"""
    goals = await goals_service.get_all()
    return paginate(goals)


@router.get("/{goal_id}", response_model=dataclasses.Goal, summary="Get goal by ID",
            status_code=HTTPStatus.OK, tags=["goals"], response_description="Goal by specific id")
async def get_goal_by_id(goal_id: UUID, goals_service: GoalService = Depends()):
    """Return single Goal by id"""
    goal = await goals_service.get_goal_by_id(goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal is not found")
    return goal


@router.get("/{goal_id}/timeunits", response_model=Page[dataclasses.Timeunit],
            summary="Get Timeunits by specific Goal",
            status_code=HTTPStatus.OK, tags=["goals"], response_description="Timeunits by specific Goal Id")
async def get_timeunits_by_goal_id(goal_id: UUID, goals_service: GoalService = Depends()):
    """Return timeunits by Goal id"""
    goal = await goals_service.get_goal_by_id(goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal is not found")
    timeunits = await goals_service.get_timeunits_by_goal_id(goal_id)

    return paginate(timeunits)


@router.post("/", summary="Add New Goal", status_code=HTTPStatus.CREATED, tags=["goals"])
async def add_goal(data: dataclasses.GoalIn, goals_service: GoalService = Depends()):
    goal = await goals_service.add_goal(data)
    if not goal:
        raise HTTPException(status_code=400, detail="Goal with such data already created")
    return goal


@router.patch("/{goal_id}", summary="Update Goal", status_code=HTTPStatus.NO_CONTENT, tags=["goals"])
async def update_goal(goal_id: UUID, data: dataclasses.GoalPatchIn, goals_service: GoalService = Depends()):
    goal = await goals_service.get_goal_by_id(goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal is not found")
    await goals_service.update_goal(goal_id, data)
    return {"msg": "Updating Successful"}


@router.delete("/{goal_id}", summary="Delete Goal", status_code=HTTPStatus.OK, tags=["goals"])
async def delete_goal(goal_id: UUID, goals_service: GoalService = Depends()):
    goal = await goals_service.delete_goal(goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal is not found")
    return {"msg": "Success", "deleted_goal": goal}
