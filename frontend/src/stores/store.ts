import { writable } from "svelte/store"
import type { Shape, Sauce, Topping, Seasoning } from "../types/type"

export const shape_id = writable<string>("");
export const shape_objects = writable<Shape[]>([]);

export const sauce_id = writable<string>("");
export const sauce_objects = writable<Sauce[]>([]);

export const toppings_id = writable<string[]>([]);
export const toppings_objects = writable<Topping[]>([]);

export const seasonings_id = writable<string[]>([]);
export const seasoning_objects = writable<Seasoning[]>([]);

//export const price = 0;