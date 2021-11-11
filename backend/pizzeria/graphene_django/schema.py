import graphene
from graphene import Mutation, String, Field, Mutation, ObjectType, ID, List
from graphene_django import DjangoObjectType
from pizzeria.models.Pizza import Shape, Sauce, Topping, Seasoning, Pizza, Order, Pizzeria
from pizzeria.models.Pizzeria import Pizzeria



class ShapeType(DjangoObjectType):
    class Meta:
        model = Shape
        fields = ("id", "name")


class SauceType(DjangoObjectType):
    class Meta:
        model = Sauce
        fields = ("id", "name")


class ToppingType(DjangoObjectType):
    class Meta:
        model = Topping
        fields = ("id", "name", "price")


class SeasoningType(DjangoObjectType):
    class Meta:
        model = Seasoning
        fields = ("id", "name", "price")


class PizzaType(DjangoObjectType):
    class Meta:
        model = Pizza
        fields = ("order", "price", "shape", "sauce", "toppings", "seasonings")


# class PizzaMutation(Mutation):
#     class Arguments:
#         shape = String(required=True)
#         sauce = String(required=True)
#         #toppings = List

#     pizza = Field(PizzaType)

#     @classmethod
#     def mutate(cls, root, info, shape, sauce, toppings, seasonings):
#         pizza = Pizza(shape=shape, sauce=sauce, toppings=toppings, seasonings=seasonings)
#         pizza.save()

#         return Pizza(pizza)
            

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ("client",)


class PizzaMutation(Mutation):
    class Arguments:
        client = String(required=True)      # input fields for mutation
        shape = ID(required=True)
        sauce = ID(required=True)
        toppings = List(ID, required=True)
        seasonings = List(ID, required=True)
    
    pizza = Field(PizzaType)

    @classmethod
    def mutate(cls, root, info, client, shape: ID, sauce: ID, toppings, seasonings):      # operations after receiving the inputs
        
        # base_price = Pizzeria.base_price      do NOT access attributes in this way, you
        # min_topping = Pizzeria.min_topping    won't be able to interact with  +, - etc. These are DeferredAttribute
        # max_topping = Pizzeria.max_topping
        # min_seasoning = Pizzeria.min_seasoning
        # max_seasoning = Pizzeria.max_seasoning

        settings = Pizzeria.objects.first()
        base_price = settings.base_price
        min_topping = settings.min_topping
        max_topping = settings.max_topping
        min_seasoning = settings.min_seasoning
        max_seasoning = settings.max_seasoning

        order = Order(client=client)
        order.save()

        toppings_list = Topping.objects.filter(pk__in=toppings)
        seasonings_list = Seasoning.objects.filter(pk__in=seasonings)

        price = base_price
        price += sum(x.price for x in toppings_list)
        price += sum(x.price for x in seasonings_list)

        print(price)

        pizza = Pizza(
            order_id = order.pk,
            shape_id = shape,
            sauce_id = sauce,
            price = price,

        )

        pizza.save()        # you need to save for an id (its pk) to be generated, which is required for setting
                            # many to many fields
        # toppings_list = Topping.objects.filter(pk__in=toppings)
        # pizza.toppings.set(toppings_list)

        # seasonings_list = Seasoning.objects.filter(pk__in=seasonings)
        # pizza.seasonings.set(seasonings_list)

        #pizza.order_pk = order.pk

        # price = base_price
        # for topping in toppings_list:
        #     price += topping.price

        # for seasoning in seasonings_list:
        #     price += seasoning.price

        return PizzaMutation(pizza)


class OrderMutation(Mutation):
    class Arguments:
        client = String(required=True)      # input fields for mutation
        shape = ID(required=True)
        sauce = ID(required=True)
        toppings = List(ID, required=True)
        seasonings = List(ID, required=True)

    order = Field(OrderType)            # subfield that can be queried after mutation

    @classmethod
    def mutate(cls, root, info, client, shape: ID, sauce: ID, toppings, seasonings):      # operations after receiving the inputs
        
        base_price = Pizzeria.base_price
        min_topping = Pizzeria.min_topping
        max_topping = Pizzeria.max_topping
        min_seasoning = Pizzeria.min_seasoning
        max_seasoning = Pizzeria.max_seasoning

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

        order = Order()
        order.client = client
        order.pizza_id = pizza.id
        order.save()

        return OrderMutation(order)


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
    #create_order = OrderMutation.Field()
    create_pizza = PizzaMutation.Field()


schema = graphene.Schema(query = Query, mutation = Mutation)