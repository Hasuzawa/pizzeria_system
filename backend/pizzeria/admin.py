from django.contrib.admin import ModelAdmin, site, StackedInline, TabularInline
from django.db.models.base import ModelBase
from .models import Shape, Sauce, Topping, Seasoning, Pizza, Order, Pizzeria

from django.db.utils import ProgrammingError

from solo.admin import SingletonModelAdmin

from .forms import PizzaForm
from django.forms import ModelChoiceField, Select


class ShapeAdmin(ModelAdmin):
    fields = ["name", "get_occurence", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated", "get_occurence"]
    list_display = ["name", "get_occurence", "date_created", "date_updated"]


class SauceAdmin(ModelAdmin):
    fields = ["name", "get_occurence", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated", "get_occurence"]
    list_display = ["name", "get_occurence", "date_created", "date_updated"]


class ToppingAdmin(ModelAdmin):
    fields = ["name", "price", "get_occurence", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated", "get_occurence"]
    list_display = ["name", "price", "get_occurence", "date_created", "date_updated"]
    list_filter = ["price"]
    search_fields = ["name"]


class SeasoningAdmin(ModelAdmin):
    fields = ["name", "price", "get_occurence", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated", "get_occurence"]
    list_display = ["name", "price", "get_occurence", "date_created", "date_updated"]
    list_filter = ["price"]


class PizzaAdmin(ModelAdmin):
    # fields = ["order", "shape", "sauce", "toppings", "seasonings", "price", "date_created", "date_updated"]
    # readonly_fields = ["date_created", "date_updated", "price"]
    list_display = ["order", "shape", "sauce", "price", "date_created", "date_updated"]
    list_filter = ["shape", "sauce"]
    search_fields = ["order"]
    # formfield_overrides = {
    #     ModelChoiceField: {
    #         "widget": Select(
    #             attrs={
    #                 "style": "width: 160px;"
    #             }
    #         )
    #     }
    # }
    form = PizzaForm


class PizzaInline(TabularInline):
    model = Pizza
    extra = 1
    

class OrderAdmin(ModelAdmin):
    fields = ["client", "completed", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated"]
    list_display = ["client", "completed", "date_created", "date_updated"]
    list_filter = ["completed"]
    search_fields = ["client"]
    inlines = [PizzaInline]


class PizzeriaAdmin(SingletonModelAdmin):
    fields = ["base_price", "min_topping", "max_topping", "min_seasoning", "max_seasoning", "date_created", "date_updated"]
    readonly_fields = ["date_created", "date_updated"]


site.register(Shape, ShapeAdmin)
site.register(Sauce, SauceAdmin)
site.register(Topping, ToppingAdmin)
site.register(Seasoning, SeasoningAdmin)

site.register(Pizza, PizzaAdmin)
site.register(Order, OrderAdmin)

site.register(Pizzeria, PizzeriaAdmin)