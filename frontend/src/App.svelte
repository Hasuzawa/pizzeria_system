<script lang="ts">
  import Header from "./components/Header.svelte"
  import Footer from "./components/Footer.svelte"
  import Body from "./components/Body.svelte"

  import { onMount } from "svelte"

  import { ApolloClient, InMemoryCache } from "@apollo/client/core"
  //import { setClient } from "svelte-apollo"

  import { createClient, initClient, setClient } from "@urql/svelte"

  // import Cookies from "js-cookie"
  // console.log(Cookies.get("csrftoken"))

  const backend_API: string = "http://127.0.0.1:8000/graphql"

  let csrf_token = "";


  const client = createClient({
    url: backend_API
  })

  setClient(client)

</script>

<svelte:head>
  <title>Pizzeria demo</title>
  <meta name="keywords"           content="pizza, reservation, demo" />
  <meta name="description"        content="Anime Lister is a compact one page application to search for anime.
      The website is created by Hasuzawa Yuichi with data fetched from AniList GraphQL API" />
  <meta name="author"             content="Hasuzawa Yuichi" />

  
  <meta property="og:locale"      content="en_US" />
  <meta property="og:type"        content="website" />
  <meta property="og:url"         content="" />
  <meta property="og:title"       content="Anime Lister by Hasuzawa Yuichi" />
  <meta property="og:description" content="The website facilitates searching anime." />

  <meta property="og:site_name"   content="Anime Lister" />

  <link rel="icon" href="/favicon.ico" />
</svelte:head>


<main class="flex flex-col">
  <Header />
  <Body />
  <Footer />
</main>


<style global lang="postcss">
  @tailwind base;
  @tailwind components;
  @tailwind utilities;

  :root {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

</style>