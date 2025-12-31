from django.db import models
from django.db.models import ExpressionWrapper, F


class CarQuerySet(models.QuerySet):
    def with_annotations(self):
        return self.select_related("model").annotate(
            car_model_id=F("model_id"),
            car_model_name=F("model__name"),
            car_model_year=F("model__year"),
            color=F("model__color"),
        )

    def as_dicts(self):
        return (
            self.with_annotations()
            .annotate(
                created_at_formatted=ExpressionWrapper(
                    models.Func(
                        models.F("created_at"),
                        function="TO_CHAR",
                        template='%(function)s(%(expressions)s, \'YYYY-MM-DD"T"HH24:MI:SS.US"Z"\')',
                    ),
                    output_field=models.CharField(),
                ),
                updated_at_formatted=ExpressionWrapper(
                    models.Func(
                        models.F("updated_at"),
                        function="TO_CHAR",
                        template='%(function)s(%(expressions)s, \'YYYY-MM-DD"T"HH24:MI:SS.US"Z"\')',
                    ),
                    output_field=models.CharField(),
                ),
            )
            .values(
                "id",
                "vin",
                "owner",
                "created_at_formatted",
                "updated_at_formatted",
                "car_model_id",
                "car_model_name",
                "car_model_year",
                "color",
            )
        )


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
