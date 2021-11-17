interface Ingredient {
    id: string
    name: string
    price: number
}

interface FreeIngredient extends Omit<Ingredient, "price"> {}

interface Shape extends FreeIngredient {}
interface AllShapes {
    allShapes: Shape[]
}


interface Sauce extends FreeIngredient {}
interface AllSauces {
    allSauces: Sauce[]
}



interface Topping extends Ingredient {}
interface AllToppings {
    allToppings: Topping[]
}


interface Seasoning extends Ingredient {}
interface AllSeasonings {
    allSeasonings: Seasoning[]
}


type CheckboxMode = "round" | "square";


interface OrderArgs {
    shapeId: string
    sauceId: string
    toppingsId: string[]
    seasoningsId: string[]
}

export type { Shape, Sauce, Topping, Seasoning, CheckboxMode, OrderArgs }
export type { AllShapes, AllSauces, AllToppings, AllSeasonings }