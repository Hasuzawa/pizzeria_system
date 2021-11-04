import { writable } from "svelte/store"

export const shape = writable<string>("round");

export const sauce = writable<string>("tomato");

export const toppings = writable<string[]>([]);

export const seasonings = writable<string[]>([]);

//export const price = 0;