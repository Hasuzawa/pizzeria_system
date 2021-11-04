import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import graphqlPlugin from "vite-plugin-graphql"

/*
import pkg from 'vite-plugin-graphql';
const { graphqlPlugin } = pkg;
*/



// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte(), graphqlPlugin]
})
