from car.views import CarsDictOrJson, CarsSerialized, CarsSerializedOrJson
from django.urls import path

urlpatterns = [
    path("api/cars-serialized/", CarsSerialized.as_view()),
    path("api/cars-orjson/", CarsSerializedOrJson.as_view()),
    path("api/cars-dict-orjson/", CarsDictOrJson.as_view()),
]

# For load-testing
urlpatterns += [
    path("api/cars/", CarsDictOrJson.as_view()),
]
