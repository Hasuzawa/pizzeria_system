interface Shape {
    name: string
}
interface AllShapes {
    allShapes: Shape[]
}


interface Sauce {
    name: string
}
interface AllSauces {
    allSauces: Sauce[]
}


interface Topping {
    name: string
    price : number
}
interface AllToppings {
    allToppings: Topping[]
}


interface Seasoning {
    name: string
    price: number
}
interface AllSeasonings {
    allSeasonings: Seasoning[]
}







export type { AllShapes, AllSauces, AllToppings, AllSeasonings }