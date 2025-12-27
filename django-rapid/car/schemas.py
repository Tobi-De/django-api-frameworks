from datetime import datetime
from rapid import Schema


class CarSchema(Schema):
    id: int
    vin: str
    owner: str
    created_at: datetime
    updated_at: datetime
    car_model_id: int
    car_model_name: str
    car_model_year: int
    color: str


class ResultsSchema(Schema):
    results: list[CarSchema]
