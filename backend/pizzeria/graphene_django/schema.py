import graphene
from graphene_django import DjangoObjectType
from pizzeria.models.Pizza import Shape, Sauce, Topping, Seasoning, Pizza, Order


class ShapeType(DjangoObjectType):
    class Meta:
        model = Shape
        fields = ("name",)


class SauceType(DjangoObjectType):
    class Meta:
        model = Sauce
        fields = ("name",)


class ToppingType(DjangoObjectType):
    class Meta:
        model = Topping
        fields = ("name",)


class SeasoningType(DjangoObjectType):
    class Meta:
        model = Seasoning
        fields = ("name",)


class PizzaType(DjangoObjectType):
    class Meta:
        model = Pizza
        fields = ("name", "price", "shape", "sauce", "toppings", "seasonings")


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ("client", "pizza")


class Query(graphene.ObjectType):
    all_shapes = graphene.List(ShapeType)
    all_sauces = graphene.List(SauceType)
    all_toppings = graphene.List(ToppingType)
    all_seasonings = graphene.List(SeasoningType)

    def resolve_all_shapes(root, info):
        return Shape.objects.all()

    def resolve_all_sauces(root, info):
        return Sauce.objects.all()

    def resolve_all_toppings(root, info):
        return Topping.objects.all()

    def resolve_all_seasonings(root, info):
        return Seasoning.objects.all()


schema = graphene.Schema(query = Query)