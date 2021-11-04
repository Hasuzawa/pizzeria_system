<script lang="ts">
  import Header from "./components/Header.svelte"
  import Footer from "./components/Footer.svelte"
  import Body from "./components/Body.svelte"

  import { ApolloClient, InMemoryCache } from "@apollo/client/core"
  //import { setClient } from "svelte-apollo"

  import { createClient, initClient, setClient } from "@urql/svelte"

  const backend_API: string = "http://127.0.0.1:8000/graphql"

  const client = createClient({
    url: backend_API
  })

  setClient(client)

  // const client = new ApolloClient({
  //   uri: backend_API,
  //   cache: new InMemoryCache(),
  //   credentials: "include"
  // });

  // setClient(client);
</script>


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