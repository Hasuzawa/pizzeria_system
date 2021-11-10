from django.db import models
from django.db.models import (Model, CharField, TextField, IntegerField, DateTimeField, ForeignKey, ManyToManyField,
    SET_NULL, Count, BooleanField, F)
from django.db.models.deletion import CASCADE, PROTECT
from .Base import TimestampBase


# django's object relational mapping allows to create table, SQL query etc without dependence on the database.
# i.e. this is database-independent SQL
# Here, each Model can be thought of as a table, and each field, a column in that table

from .Pizzeria import Pizzeria


class Shape(TimestampBase):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_occurence(self) -> int:
        #print(Pizzeria.objects.first().base_price)
        return Pizza.objects.filter(shape__pk=self.pk).count()
    get_occurence.admin_order_field = "pk"
    get_occurence.short_description = "ordered"


class Sauce(TimestampBase):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_occurence(self) -> int:
        return Pizza.objects.filter(sauce__pk=self.pk).count()
    get_occurence.admin_order_field = "pk"
    get_occurence.short_description = "ordered"


class Topping(TimestampBase):
    name = CharField(max_length=255)
    price = IntegerField()

    def get_occurence(self) -> int:
        return Pizza.objects.filter(toppings__pk=self.pk).count()   # count pizzas with this topping
    get_occurence.admin_order_field = "pk"
    get_occurence.short_description = "ordered"

    def __str__(self):
        return self.name


class Seasoning(TimestampBase):
    name = CharField(max_length=255)
    price = IntegerField()

    def __str__(self):
        return self.name

    def get_occurence(self) -> int:
        return Pizza.objects.filter(seasonings__pk=self.pk).count()
    get_occurence.admin_order_field = "pk"
    get_occurence.short_description = "ordered"


class Pizza(TimestampBase):
    #name = CharField(max_length=255, null=True)
    #price = IntegerField()

    shape = ForeignKey(Shape, null=True, on_delete=PROTECT)
    sauce = ForeignKey(Sauce, null=True, on_delete=PROTECT)
    toppings = ManyToManyField(Topping)
    seasonings = ManyToManyField(Seasoning)

    def __str__(self):
        return "{}, {}, {} topping, {} seasoning".format(
            self.shape, self.sauce, self.toppings.count(), self.seasonings.count())


class Order(TimestampBase):
    # in a real setting, it is common to use phone number, email address for identification and contact, but here
    # we simplify it by using a name
    client = CharField(max_length=255)
    pizza = ForeignKey(Pizza, null=True, on_delete=CASCADE)
    completed = BooleanField(default=False)

    def __str__(self):
        return "{} by {}".format(self.pizza, self.client)