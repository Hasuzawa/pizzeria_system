from django.db import models
from django.db.models import (Model, CharField, TextField, IntegerField, DateTimeField, ForeignKey, ManyToManyField,
    SET_NULL)
from .Base import TimestampBase

# django's object relational mapping allows to create table, SQL query etc without dependence on the database.
# i.e. this is database-independent SQL
# Here, each Model can be thought of as a table, and each field, a column in that table


class Shape(TimestampBase):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Sauce(TimestampBase):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Topping(TimestampBase):
    name = CharField(max_length=255)
    price = IntegerField()

    def __str__(self):
        return self.name


class Seasoning(TimestampBase):
    name = CharField(max_length=255)
    price = IntegerField()

    def __str__(self):
        return self.name


class Order(TimestampBase):
    shape = ForeignKey(Shape, null=True, on_delete=SET_NULL)
    sauce = ForeignKey(Sauce, null=True, on_delete=SET_NULL)
    toppings = ManyToManyField(Topping)
    seasonings = ManyToManyField(Seasoning)

    price = IntegerField()  #derived field

    def __str__(self):
        return "{} {} pizza with {} topping and {} seasoning".format(
            self.shape, self.sauce, len(self.toppings), len(self.seasonings))