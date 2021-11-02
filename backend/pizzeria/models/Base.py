from django.db import models
from django.db.models import (Model, CharField, TextField, IntegerField, DateTimeField, ForeignKey, ManyToManyField,
    SET_NULL)


class TimestampBase(Model):
    date_created = DateTimeField(auto_now_add=True)
    date_updated = DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Singleton(Model):
    pass
