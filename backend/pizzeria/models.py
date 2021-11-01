from django.db import models
from django.db.models import Model, CharField, TextField, IntegerField, DateTimeField, ForeignKey, SET_NULL

# django's object relational mapping allows to create table, SQL query etc without dependence on the database.
# i.e. this is database-independent SQL
# Here, each Model can be thought of as a table, and each field, a column in that table


class Shape(Model):
    name = CharField(max_length=255)
    date_created = DateTimeField(auto_now_add=True)
    date_updated = DateTimeField(auto_now=True)


class Sauce(Model):
    name = CharField(max_length=255)
    date_created = DateTimeField(auto_now_add=True)
    date_updated = DateTimeField(auto_now=True)


class Topping(Model):
    name = CharField(max_length=255)
    price = IntegerField()


class Seasoning(Model):
    name = CharField(max_length=255)
    price = IntegerField()


class Order(Model):
    price = IntegerField()
    shape = ForeignKey(Shape, null=True, on_delete=SET_NULL)
    sauce = ForeignKey(Sauce, null=True, on_delete=SET_NULL)
    #toppings
    #seasonings 
    date_created = DateTimeField(auto_now_add=True)