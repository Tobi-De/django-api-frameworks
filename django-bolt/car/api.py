from datetime import datetime

from django_bolt import BoltAPI
from django_bolt.serializers import Serializer

from car.models import Car

api = BoltAPI()


class CarSerializer(Serializer):
    id: int
    vin: str
    owner: str
    created_at: datetime
    updated_at: datetime
    car_model_id: int
    car_model_name: str
    car_model_year: int
    color: str


@api.get("/cars-serialized")
async def cars():
    cars = []

    async for car in Car.objects.with_annotations():
        cars.append(CarSerializer.from_model(car))

    return {"results": cars}


@api.get("/cars-dicts")
async def cars_as_dicts() -> dict[str, list[dict]]:
    cars = []

    async for car_dict in Car.objects.as_dicts().aiterator():
        cars.append(car_dict)

    return {"results": cars}
