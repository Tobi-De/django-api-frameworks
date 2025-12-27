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
def test_list_cars_with_schema(api_client, create_test_data):
    response = api_client.get("/ninja/with-schema/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["vin"] == "VIN-123"
    assert data[0]["car_model_name"] == "Test Model"


@pytest.mark.django_db
def test_list_cars_without_schema(api_client, create_test_data):
    response = api_client.get("/ninja/without-schema/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["vin"] == "VIN-123"
    assert data[0]["car_model_name"] == "Test Model"
