from django.urls import path

from car.views import Cars, CarsOrJson, CarsModelToDict, CarsQuerysetToDict

urlpatterns = [
    path("cars-json/", Cars.as_view()),
    path("cars-orjson/", CarsOrJson.as_view()),
    path("cars-model-to-dict/", CarsModelToDict.as_view()),
    path("cars-queryset-as-dicts/", CarsQuerysetToDict.as_view()),
]

# For load-testing
urlpatterns += [
    path("cars/", Cars.as_view()),
]
