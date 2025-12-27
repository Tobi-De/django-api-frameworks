from django.urls import path
from ninja import NinjaAPI
from car.views import router
from custom_renderer import ORJSONRenderer

# api = NinjaAPI()
api = NinjaAPI(renderer=ORJSONRenderer())

api.add_router("", router)


urlpatterns = [
    path("api/", api.urls),
]
