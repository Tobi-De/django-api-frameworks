from rest_framework import serializers

"""
Skip ModelSerializer because it's much slower.
"""


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    vin = serializers.CharField()
    owner = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    car_model_id = serializers.IntegerField(source="model_id")
    car_model_name = serializers.CharField(source="model.name")
    car_model_year = serializers.IntegerField(source="model.year")
    color = serializers.CharField(source="model.color")
