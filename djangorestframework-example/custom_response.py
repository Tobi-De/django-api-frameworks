import orjson
from django.db.models import QuerySet
from django.http import HttpResponse


def orjson_serialize(obj):
    if hasattr(obj, "isoformat"):
        return obj.isoformat()[:-6] + "Z"

    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


class OrJsonResponse(HttpResponse):
    def __init__(self, data, json_dumps_params=None, *args, **kwargs):
        if json_dumps_params is None:
            json_dumps_params = {}

        kwargs.setdefault("content_type", "application/json")

        if isinstance(data, QuerySet):
            data = list(data)

        data = orjson.dumps(data, **json_dumps_params, default=orjson_serialize)

        super().__init__(content=data, **kwargs)
