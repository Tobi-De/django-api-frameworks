from car.api import api as cars_api
from django_bolt import BoltAPI

api = BoltAPI()

api.mount("/api", cars_api)
