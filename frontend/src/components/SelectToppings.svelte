<script lang="ts">
    import type { AllToppings } from "src/types/type";
    import { operationStore, query } from "@urql/svelte"
    import Card from "./Card.svelte"

    const toppingQuery = operationStore<AllToppings>(`
        query {
            allToppings {
                price
                name
            }
        }
    `)

    query(toppingQuery);

</script>

<div>
    <h1>Select your Toppings</h1>
    {#if $toppingQuery.fetching}
        <span>loading</span>
    {:else if $toppingQuery.error}
        <span>data fetching failed</span>
    {:else}
        <div class="flex flex-row">
        {#each $toppingQuery.data.allToppings as topping}
            <Card name={topping.name} />
        {/each}
        </div>
    {/if}
</div>