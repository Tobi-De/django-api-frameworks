import pytest
from django.test import Client

from car.models import Car, CarModel


@pytest.fixture
def api_client():
    return Client()


@pytest.fixture
def create_test_data(db):
    model = CarModel.objects.create(
        name="Test Model",
        make="Test Make",
        year=2024,
        color="Red",
        price=50000.00,
    )
    Car.objects.create(vin="VIN-123", model=model, owner="Test Owner")


@pytest.mark.django_db
def test_list_cars(api_client, create_test_data):
    response = api_client.get("/api/cars/")

    assert response.status_code == 200
    data = response.json()
    assert len(data["results"]) == 1
    assert data["results"][0]["vin"] == "VIN-123"
    assert data["results"][0]["car_model_name"] == "Test Model"
