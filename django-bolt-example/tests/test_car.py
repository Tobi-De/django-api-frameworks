import pytest
from car.api import api
from car.models import Car, CarModel
from django_bolt.testing import TestClient


@pytest.fixture(autouse=True)
def setup_db(db):
    """Clean database before and after each test."""

    Car.objects.all().delete()
    CarModel.objects.all().delete()

    model = CarModel.objects.create(
        name="Test Model",
        make="Test Make",
        year=2024,
        color="Red",
        price=50000.00,
    )
    Car.objects.create(vin="VIN-123", model=model, owner="Test Owner")

    yield

    Car.objects.all().delete()
    CarModel.objects.all().delete()


@pytest.mark.django_db(transaction=True)
def test_list_cars():
    with TestClient(api) as client:
        response = client.get("/cars/")
        assert 200 == response.status_code

        actual = response.json()
        results = actual["results"]
        assert 1 == len(results)
        assert "VIN-123" == results[0]["vin"]
        assert "Test Model" == results[0]["car_model_name"]
