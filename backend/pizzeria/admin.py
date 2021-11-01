from django.contrib.admin import ModelAdmin, site
from django.db.models.base import ModelBase
from .models import Shape, Sauce, Topping, Seasoning, Order


# class TimestampAdmin(ModelBase):
#     fields = ["date_created", "date_updated"]
#     readonly_fields = ["date_created", "date_updated"]

#     class Meta:
#         abstract = True


class ShapeAdmin(ModelAdmin):
    fields = ["name", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated"]


class SauceAdmin(ModelAdmin):
    fields = ["name", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated"]


class ToppingAdmin(ModelAdmin):
    fields = ["name", "price", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated"]


class SeasoningAdmin(ModelAdmin):
    fields = ["name", "price", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated"]


class Order(ModelAdmin):
    pass


site.register(Shape, ShapeAdmin)
site.register(Sauce, SauceAdmin)
site.register(Topping, ToppingAdmin)
site.register(Seasoning, SeasoningAdmin)