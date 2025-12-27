from typing import Annotated

from database import get_db
from services.cars import CarService
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends

router = APIRouter()

from datetime import datetime

from pydantic import BaseModel


class CarSchema(BaseModel):
    id: int
    vin: str
    owner: str
    created_at: datetime
    updated_at: datetime
    car_model_id: int
    car_model_name: str
    car_model_year: int
    color: str


@router.get("/cars/", response_model=dict[str, list[CarSchema]])
async def list_cars(db: Annotated[AsyncSession, Depends(get_db)]):
    cars = await CarService(db).retrieve_all_cars()

    return {"results": cars}
