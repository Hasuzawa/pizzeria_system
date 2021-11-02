<script lang="ts">
  import Header from "./components/Header.svelte"
  import Footer from "./components/Footer.svelte"
  import Body from "./components/Body.svelte"
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