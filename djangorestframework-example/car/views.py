from custom_response import OrJsonResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from car.models import Car
from car.serializers import CarSerializer


class CarsSerialized(APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        cars = Car.objects.all().select_related("model")
        serializer = CarSerializer(cars, many=True)

        return Response({"results": serializer.data}, status=status.HTTP_200_OK)


class CarsSerializedOrJson(APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        cars = Car.objects.all().select_related("model")
        serializer = CarSerializer(cars, many=True)

        return OrJsonResponse({"results": serializer.data}, status=status.HTTP_200_OK)


class CarsDictOrJson(APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        cars = Car.objects.all().as_dicts()

        return OrJsonResponse({"results": cars}, status=status.HTTP_200_OK)
