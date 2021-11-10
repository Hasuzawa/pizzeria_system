import graphene
from graphene import Mutation, String, Field, Mutation, ObjectType, ID, List
from graphene_django import DjangoObjectType
from pizzeria.models.Pizza import Shape, Sauce, Topping, Seasoning, Pizza, Order
from pizzeria.models.Pizzeria import Pizzeria


class ShapeType(DjangoObjectType):
    class Meta:
        model = Shape
        fields = ("name",)


class SauceType(DjangoObjectType):
    class Meta:
        model = Sauce
        fields = ("name",)

# class SauceMutation(Mutation):
#     class Arguments:
#         name = String(required=True)

#     sauce = Field(SauceType)

#     @classmethod
#     def mutate(cls, root, info, name: str):
#         sauce = Sauce(name=name)
#         sauce.save()

#         return SauceMutation(sauce)


class ToppingType(DjangoObjectType):
    class Meta:
        model = Topping
        fields = ("name", "price")


class SeasoningType(DjangoObjectType):
    class Meta:
        model = Seasoning
        fields = ("name", "price")


class PizzaType(DjangoObjectType):
    class Meta:
        model = Pizza
        fields = ("shape", "sauce", "toppings", "seasonings")

class PizzaMutation(Mutation):
    class Arguments:
        shape = String(required=True)
        sauce = String(required=True)
        #toppings = List

    pizza = Field(PizzaType)

    @classmethod
    def mutate(cls, root, info, shape, sauce, toppings, seasonings):
        pizza = Pizza(shape=shape, sauce=sauce, toppings=toppings, seasonings=seasonings)
        pizza.save()

        return Pizza(pizza)
            


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ("client", "pizza")

class OrderMutation(Mutation):
    class Arguments:
        client = String(required=True)      # input fields for mutation

        shape = ID(required=True)
        sauce = ID(required=True)
        toppings = List(ID, required=True)
        seasonings = List(ID, required=True)

    order = Field(OrderType)            # subfield that can be queried after mutation
    pizza = Field(PizzaType)

    @classmethod
    def mutate(cls, root, info, client, shape: ID, sauce: ID, toppings, seasonings):      # operations after receiving the inputs

        pizza = Pizza()
        pizza.shape_id = shape
        pizza.sauce_id = sauce

        pizza.save()        # you need to save for an id (its pk) to be generated, which is required for setting
                            # many to many fields

        toppings_list = Topping.objects.filter(pk__in=toppings)
        pizza.toppings.set(toppings_list)

        seasonings_list = Seasoning.objects.filter(pk__in=seasonings)
        pizza.seasonings.set(seasonings_list)

        pizza.save()

        return OrderMutation(pizza)


class PizzeriaType(DjangoObjectType):
    class Meta:
        model = Pizzeria
        fields = ("base_price", "min_topping", "max_topping", "min_seasoning", "max_seasoning")


class Query(ObjectType):
    all_shapes = List(ShapeType)
    all_sauces = List(SauceType)
    all_toppings = List(ToppingType)
    all_seasonings = List(SeasoningType)
    order_info = Field(PizzeriaType)       # singleton

    def resolve_all_shapes(root, info):
        print("testing")
        return Shape.objects.all()

    def resolve_all_sauces(root, info):
        return Sauce.objects.all()

    def resolve_all_toppings(root, info):
        return Topping.objects.all()

    def resolve_all_seasonings(root, info):
        return Seasoning.objects.all()

    def resolve_order_info(root, info):
        return Pizzeria.objects.first()


class Mutation(ObjectType):
    create_order = OrderMutation.Field()


schema = graphene.Schema(query = Query, mutation = Mutation)