from car.views import CarListingAPI
from django.urls import path

urlpatterns = [
    path("api/cars/", CarListingAPI.as_view()),
]
