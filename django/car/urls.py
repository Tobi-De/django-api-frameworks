from django.urls import path

from car import views

urlpatterns = [
    path("cars/sync/", views.cars_sync),
    path("cars/async/", views.cars_async),
    path("cars/streaming/", views.cars_streaming),
    path("cars/asyncpg/", views.cars_asyncpg),
]

# For load-testing
urlpatterns += [
    path("cars/", views.cars_sync),
]
