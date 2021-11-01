from django.db import models
from django.db.models import (Model, CharField, TextField, IntegerField, DateTimeField, ForeignKey, ManyToManyField,
    SET_NULL)
from .Base import Singleton


class Pizzeria(Singleton):
    pass