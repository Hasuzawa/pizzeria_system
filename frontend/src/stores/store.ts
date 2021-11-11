import { writable } from "svelte/store"
//import type { Shape, Sauce, Topping, Seasoning } from "../types/type"

export const shapeId = writable<string>("");
export const shapeName = writable<string>("");

export const sauceId = writable<string>("");
export const sauceName = writable<string>("");

export const toppingsId = writable<string[]>([]);

export const seasoningsId = writable<string[]>([]);


//export const price = 0;