from django.db import models
from django.db.models import F


class CarQuerySet(models.QuerySet):
    def with_annotations(self):
        return self.select_related("model").annotate(
            car_model_id=F("model_id"),
            car_model_name=F("model__name"),
            car_model_year=F("model__year"),
            color=F("model__color"),
        )

    def as_dicts(self):
        queryset = self.with_annotations()
        result = []

        for item in queryset:
            result.append(
                {
                    "id": item.id,
                    "vin": item.vin,
                    "owner": item.owner,
                    "created_at": item.created_at.isoformat().replace("+00:00", "Z"),
                    "updated_at": item.updated_at.isoformat().replace("+00:00", "Z"),
                    "car_model_id": item.car_model_id,
                    "car_model_name": item.car_model_name,
                    "car_model_year": item.car_model_year,
                    "color": item.color,
                }
            )
        return result


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Car(models.Model):
    vin = models.CharField(max_length=17)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    owner = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CarQuerySet.as_manager()
