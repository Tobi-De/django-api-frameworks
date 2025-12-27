from car.views import router
from custom_renderer import ORJSONRenderer
from django.urls import path
from ninja import NinjaAPI

# Default renderer
# api = NinjaAPI()

# ORJSON renderer
api = NinjaAPI(renderer=ORJSONRenderer())

api.add_router("", router)


urlpatterns = [
    path("api/", api.urls),
]
