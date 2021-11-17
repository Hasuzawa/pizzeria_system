<script lang="ts">
    import type { AllToppings } from "src/types/type";
    import { operationStore, query } from "@urql/svelte"
    import MultiCard from "./MultiCard.svelte"

    import { toppingsId } from "../../stores/store"

    const toppingQuery = operationStore<AllToppings>(`
        query {
            allToppings {
                id
                price
                name
            }
            
        }
    `)

    query(toppingQuery);

</script>


<div class="w-full flex flex-col items-center">
    <h1>Your favorite toppings</h1>
    {#if $toppingQuery.fetching}
        <span>loading</span>
    {:else if $toppingQuery.error}
        <span>data fetching failed</span>
    {:else}
        <div class="flex flex-row flex-wrap justify-center gap-x-4 gap-y-6 mt-4 mb-2">
        {#each $toppingQuery.data.allToppings as topping}
            <MultiCard
                id={topping.id}
                name={topping.name}
                price={topping.price}
                writableIds={toppingsId}
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