import django.urls.converters
from django.urls.converters import register_converter as original_register_converter


# Moneypatch to support Django 6
def register_converter_silent(converter, type_name):
    try:
        original_register_converter(converter, type_name)
    except ValueError:
        pass


django.urls.converters.register_converter = register_converter_silent
from django import urls

urls.register_converter = register_converter_silent
