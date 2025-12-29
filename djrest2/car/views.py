from django.db.models import QuerySet
from django.forms.models import model_to_dict
from djrest import ListCreateView

from car.custom_response import OrJsonResponse
from car.forms import CarForm
from car.models import Car


class Cars(ListCreateView):
    model = Car
    form_class = CarForm

    def get_queryset(self):
        return Car.objects.with_annotations()


class CarsOrJson(ListCreateView):
    model = Car
    form_class = CarForm
    response_class = OrJsonResponse

    def get_queryset(self):
        return Car.objects.with_annotations()


class CarsModelToDict(ListCreateView):
    model = Car
    form_class = CarForm

    def serialize_one(self, obj):
        return model_to_dict(obj)


class CarsQuerysetToDict(CarsModelToDict):
    def serialize(self, obj_or_qs):
        if isinstance(obj_or_qs, QuerySet):
            return list(obj_or_qs.as_dicts())
        return super().serialize(obj_or_qs)
