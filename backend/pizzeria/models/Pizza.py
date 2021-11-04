from django.db import models
from django.db.models import (Model, CharField, TextField, IntegerField, DateTimeField, ForeignKey, ManyToManyField,
    SET_NULL)
from django.db.models.deletion import CASCADE, PROTECT
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


class Pizza(TimestampBase):
    #name = CharField(max_length=255, null=True)
    #price = IntegerField()

    shape = ForeignKey(Shape, null=True, on_delete=PROTECT)
    sauce = ForeignKey(Sauce, null=True, on_delete=PROTECT)
    toppings = ManyToManyField(Topping)
    seasonings = ManyToManyField(Seasoning)


    def __str__(self):
        return "{} {} pizza with {} topping and {} seasoning".format(
            self.shape, self.sauce, len(self.toppings), len(self.seasonings))


class Order(TimestampBase):
    # in a real setting, it is common to use phone number, email address for identification and contact, but here
    # we simplify it by using a name
    client = CharField(max_length=255)
    pizza = ForeignKey(Pizza, null=True, on_delete=CASCADE)

    def __str__(self):
        return "{} by {}".format(self.pizza, self.client)