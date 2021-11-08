<script lang="ts">
    import type { AllToppings } from "src/types/type";
    import { operationStore, query } from "@urql/svelte"
    import MultiCard from "./MultiCard.svelte"

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


<div class="flex flex-col items-center">
    <h1>Select your Toppings</h1>
    {#if $toppingQuery.fetching}
        <span>loading</span>
    {:else if $toppingQuery.error}
        <span>data fetching failed</span>
    {:else}
        <div class="flex flex-row flex-wrap">
        {#each $toppingQuery.data.allToppings as topping}
            <MultiCard
                name={topping.name}
                price={topping.price}

            />
        {/each}
        </div>
    {/if}
</div>


<style lang="postcss">
    h1 {
        font-size: 30px;
    }
</style>