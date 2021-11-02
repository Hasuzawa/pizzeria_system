from django.db import models
from django.db.models import (Model, CharField, TextField, IntegerField, DateTimeField, ForeignKey, ManyToManyField,
    SET_NULL, )
from .Base import Singleton


# The usage of IntegerField instead of PositiveIntegerField is intentional

class Pizzeria(Singleton):
    min_topping = IntegerField(default=3)
    max_topping = IntegerField(default=10)
    min_seasoning = IntegerField(default=0)
    max_seasoning = IntegerField(default=None)

