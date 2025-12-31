from rapid import APIView, validate

from car.models import Car
from car.schemas import ResultsSchema


class CarListingAPI(APIView):
    @validate(response_schema=ResultsSchema)
    def get(self, request):
        cars = Car.objects.with_annotations()
        results = list(cars.as_dicts())

        return ResultsSchema(results=results)
