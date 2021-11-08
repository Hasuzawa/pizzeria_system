import { writable } from "svelte/store"

export const shape = writable<string>("");

export const sauce = writable<string>("");

export const toppings = writable<string[]>([]);

export const seasonings = writable<string[]>([]);

//export const price = 0;