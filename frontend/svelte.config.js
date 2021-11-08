import sveltePreprocess from 'svelte-preprocess'
import autoPreprocess from "svelte-preprocess"

// a default can be set so you don't need to keep writing ts, postcss
// https://qiita.com/mkin/items/ef0c8308cd167f36709d


export default {
  // Consult https://github.com/sveltejs/svelte-preprocess
  // for more information about preprocessors
  preprocess: sveltePreprocess()
}
