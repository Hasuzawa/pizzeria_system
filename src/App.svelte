<script lang="ts">
  import Header from "./components/Header.svelte"
  import Footer from "./components/Footer.svelte"
</script>

<main class="flex flex-col">
  <Header />
  <div class="flex-1">
    
  </div>
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