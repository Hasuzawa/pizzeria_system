from django.contrib.admin import ModelAdmin, site
from django.db.models.base import ModelBase
from .models import Shape, Sauce, Topping, Seasoning, Pizza, Order, Pizzeria

from django.db.utils import ProgrammingError

from solo.admin import SingletonModelAdmin

# class TimestampAdmin(ModelBase):
#     fields = ["date_created", "date_updated"]
#     readonly_fields = ["date_created", "date_updated"]

#     class Meta:
#         abstract = True


class ShapeAdmin(ModelAdmin):
    fields = ["name", "get_occurence", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated", "get_occurence"]
    list_display = ["name", "get_occurence", "date_created", "date_updated"]


class SauceAdmin(ModelAdmin):
    fields = ["name", "get_occurence", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated", "get_occurence"]
    list_display = ["name", "get_occurence", "date_created", "date_updated"]


class ToppingAdmin(ModelAdmin):
    fields = ["name", "price", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated"]
    list_display = ["name", "price", "date_created", "date_updated"]
    list_filter = ["price"]


class SeasoningAdmin(ModelAdmin):
    fields = ["name", "price", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated"]
    list_display = ["name", "price", "date_created", "date_updated"]
    list_filter = ["price"]


class PizzaAdmin(ModelAdmin):
    #fields = ["name", "price", "shape", "sauce", "toppings", "seasonings"]
    fields = ["shape", "sauce", "toppings", "seasonings"]
    list_display = ["__str__", "shape", "sauce"]
    

class OrderAdmin(ModelAdmin):
    fields = ["client", "pizza", "completed"]
    list_display = ["client", "pizza", "completed"]
    list_filter = ["completed"]


class PizzeriaAdmin(SingletonModelAdmin):
    fields = ["base_price", "min_topping", "max_topping", "min_seasoning", "max_seasoning", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated"]
    # help_texts = {
    #     "min_topping": "The minimum topping for an order, defaults to 3",
    #     "max_topping": "The maximum topping for an order, defaults to 10."
    # }

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
site.register(Pizzeria, PizzeriaAdmin)