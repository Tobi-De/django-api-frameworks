from djrest import ListCreateView

from car.forms import CarForm
from car.models import Car


class CarListingAPI(ListCreateView):
    model = Car
    form_class = CarForm

    def get_queryset(self):
        return Car.objects.with_annotations()
