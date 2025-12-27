import orjson
from django.db.models import F
from django.http import HttpResponse, StreamingHttpResponse

from car.asyncpg_manager import AsyncpgManager
from car.models import Car


def orjson_serialize(obj):
    if hasattr(obj, "isoformat"):
        return obj.isoformat()[:-6] + "Z"

    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


def cars_sync(request):
    """
    Returns a list of cars with their model information.
    """

    cars_queryset = (
        Car.objects.select_related("model")
        .annotate(
            car_model_id=F("model_id"),
            car_model_name=F("model__name"),
            car_model_year=F("model__year"),
            color=F("model__color"),
        )
        .values(
            "id",
            "vin",
            "owner",
            "created_at",
            "updated_at",
            "car_model_id",
            "car_model_name",
            "car_model_year",
            "color",
        )
    )

    return HttpResponse(
        orjson.dumps(
            {"results": list(cars_queryset)},
            option=orjson.OPT_PASSTHROUGH_DATETIME,
            default=orjson_serialize,
        ),
        content_type="application/json",
    )


async def cars_async(request):
    """
    Returns a list of cars with their model information.
    Optimized version using custom queryset method and aiterator().
    """

    # Use the custom queryset method for cleaner code
    cars_queryset = Car.objects.as_dicts()

    # Use aiterator() for better memory efficiency with large datasets
    cars_list = []
    async for car in cars_queryset.aiterator():
        cars_list.append(car)

    return HttpResponse(
        orjson.dumps(
            {"results": cars_list},
            option=orjson.OPT_PASSTHROUGH_DATETIME,
            default=orjson_serialize,
        ),
        content_type="application/json",
    )


async def cars_streaming(request):
    """
    Returns a list of cars with their model information.
    """

    cars_queryset = (
        Car.objects.select_related("model")
        .annotate(
            car_model_id=F("model_id"),
            car_model_name=F("model__name"),
            car_model_year=F("model__year"),
            color=F("model__color"),
        )
        .values(
            "id",
            "vin",
            "owner",
            "created_at",
            "updated_at",
            "car_model_id",
            "car_model_name",
            "car_model_year",
            "color",
        )
    )

    def generate():
        yield '{"results": ['
        first = True

        for car in cars_queryset.iterator(chunk_size=1000):  # Process in chunks
            if not first:
                yield ","

            first = False

            yield orjson.dumps(car, option=orjson.OPT_PASSTHROUGH_DATETIME, default=orjson_serialize)

        yield "]}"

    response = StreamingHttpResponse(generate(), content_type="application/json")
    response["Cache-Control"] = "no-cache"

    return response


async def cars_asyncpg(request):
    """
    Use asyncpg directly.
    """

    cars_list = await AsyncpgManager().get_cars()

    return HttpResponse(
        orjson.dumps(
            {"results": cars_list},
            option=orjson.OPT_PASSTHROUGH_DATETIME,
            default=orjson_serialize,
        ),
        content_type="application/json",
    )
