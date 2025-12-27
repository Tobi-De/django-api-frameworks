import orjson
from ninja.renderers import BaseRenderer


def orjson_serialize(obj):
    if hasattr(obj, "isoformat"):
        return obj.isoformat()[:-6] + "Z"

    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(
            data,
            option=orjson.OPT_PASSTHROUGH_DATETIME,
            default=orjson_serialize,
        )
