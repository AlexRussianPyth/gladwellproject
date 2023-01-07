from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate

from src.models import dataclasses
from src.services.timeunits import TimeunitsService


router = APIRouter()


@router.get(
    "/",
    response_model=Page[dataclasses.Timeunit],
    summary="Get All Timeunits",
    status_code=HTTPStatus.OK,
    tags=["timeunits"],
    response_description="All Timeunits in Database")
async def get_all_timeunits(timeunits_service: TimeunitsService = Depends()):
    """Return all Timeunits in database"""
    timeunits = await timeunits_service.get_all()
    print(timeunits)
    return paginate(timeunits)


@router.get("/{timeunit_id}", response_model=dataclasses.Timeunit, summary="Get Timeunit by ID",
            status_code=HTTPStatus.OK, tags=["timeunits"], response_description="Timeunit by specific id")
async def get_timeunit_by_id(timeunit_id: UUID, timeunits_service: TimeunitsService = Depends()):
    """Return Single Timeunit by ID"""
    timeunit = await timeunits_service.get_timeunit_by_id(timeunit_id)
    if not timeunit:
        raise HTTPException(status_code=404, detail="Timeunit is not found")
    return timeunit


@router.post("/", summary="Add New Timeunit", status_code=HTTPStatus.CREATED, tags=["timeunits"])
async def add_timeunit(data: dataclasses.TimeunitIn, timeunits_service: TimeunitsService = Depends()):
    timeunit = await timeunits_service.add_timeunit(data)
    if not timeunit:
        raise HTTPException(status_code=400, detail="Timeunit with such data already created")
    return timeunit


@router.patch("/{timeunit_id}", summary="Update Timeunit", status_code=HTTPStatus.NO_CONTENT, tags=["timeunits"])
async def update_timeunit(timeunit_id: UUID, data: dataclasses.TimeunitPatchIn,
                          timeunits_service: TimeunitsService = Depends()):
    timeunit = await timeunits_service.get_timeunit_by_id(timeunit_id)
    if not timeunit:
        raise HTTPException(status_code=404, detail="Timeunit is not found")
    await timeunits_service.update_timeunit(timeunit_id, data)
    return {"msg": "Updating Successful"}


@router.delete("/{timeunit_id}", summary="Delete Timeunit", status_code=HTTPStatus.OK, tags=["timeunits"])
async def delete_timeunit(timeunit_id: UUID, timeunits_service: TimeunitsService = Depends()):
    timeunit = await timeunits_service.delete_timeunit(timeunit_id)
    if not timeunit:
        raise HTTPException(status_code=404, detail="Timeunit is not found")
    return {"msg": "Success", "deleted_timeunit": timeunit}
