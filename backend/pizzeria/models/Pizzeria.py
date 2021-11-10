from django.db import models
from django.db.models import (Model, CharField, TextField, IntegerField, DateTimeField, ForeignKey, ManyToManyField,
    SET_NULL, )
from solo.models import SingletonModel
from .Base import TimestampBase


# The usage of IntegerField instead of PositiveIntegerField is intentional

class Pizzeria(SingletonModel, TimestampBase):
    base_price = IntegerField(default=10, help_text="The base price of a pizza, without any topping and seasoning.")
    min_topping = IntegerField(default=3, help_text="The minimum topping for an order, defaults to 3.")
    max_topping = IntegerField(null=True, blank=True, default=10,
        help_text="The maximum topping for an order, defaults to 10. Leave it empty to have no upper limit.")
    min_seasoning = IntegerField(default=0, help_text="The minimum seasoning for an order, defaults to 0.")
    max_seasoning = IntegerField(null=True, blank=True, default=None,
        help_text="The maximum seasoning for an order, defaults to 10. Leave it empty to have no upper limit.")

    def __str__(self):
        return "settings for the whole site"