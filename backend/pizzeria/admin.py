from django.contrib.admin import ModelAdmin, site
from django.db.models.base import ModelBase
from .models import Shape, Sauce, Topping, Seasoning, Pizza, Order

from django.db.utils import ProgrammingError


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


class PizzaAdmin(ModelAdmin):
    #fields = ["name", "price", "shape", "sauce", "toppings", "seasonings"]
    fields = ["shape", "sauce", "toppings", "seasonings"]
    

class OrderAdmin(ModelAdmin):
    fields = ["client", "pizza"]


# class PizzeriaAdmin(ModelAdmin):
#     fields = ["min_topping", "max_topping", "min_seasoning", "max_seasoning"]

#     def __init__(self, model, admin_site):
#         super().__init__(model, admin_site)

#         #try:
#         #    Pizzeria.load().save()
#         #except ProgrammingError:
#         #    pass
 
#     def has_add_permission(self, request, obj=None):
#         return False
 
#     def has_delete_permission(self, request, obj=None):
#         return False



site.register(Shape, ShapeAdmin)
site.register(Sauce, SauceAdmin)
site.register(Topping, ToppingAdmin)
site.register(Seasoning, SeasoningAdmin)

site.register(Pizza, PizzaAdmin)
site.register(Order, OrderAdmin)

#site.register(Pizzeria, PizzeriaAdmin)