from django.forms import (ModelForm, CharField, IntegerField, ModelChoiceField, TextInput, Textarea, NumberInput, Select,
    SelectMultiple, CheckboxSelectMultiple, DateTimeField)
from .models.Pizza import Shape, Sauce, Topping, Seasoning, Pizza, Order
from django.utils.safestring import mark_safe

short_field = {
    "style": "width: 80px"
}
normal_field = {
    "style": "width: 120px"
}
long_field = {
    "style": "width: 160px"
}

class PizzaForm(ModelForm):
    order = ModelChoiceField(
        queryset=Order.objects.all(),
        widget=Select(attrs=long_field)
    )
    price = IntegerField(
        help_text=mark_safe("The price is calculated at creation time. Changing prices in database will only affect prices of pizza made afterward."),
        widget=NumberInput(attrs=short_field)
    )
    shape = ModelChoiceField(
        queryset=Shape.objects.all(),
        widget=Select(attrs=long_field)
    )
    sauce = ModelChoiceField(
        queryset=Sauce.objects.all(),
        widget=Select(attrs=long_field)
    )
    toppings = ModelChoiceField(
        queryset=Topping.objects.all(),
        widget=CheckboxSelectMultiple(attrs={
            # "rows": 100,
            # "cols": 50
        })
    )
    seasonings = ModelChoiceField(
        queryset=Seasoning.objects.all(),
        widget=CheckboxSelectMultiple(attrs={
            
        })
    )

    class Meta:
        model = Pizza
        fields = ("order", "price", "shape", "sauce", "toppings", "seasonings",)