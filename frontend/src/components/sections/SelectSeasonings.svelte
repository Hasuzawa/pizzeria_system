<script lang="ts">
    import type { AllSeasonings } from "src/types/type";
    import { operationStore, query } from "@urql/svelte"
    import MultiCard from "./MultiCard.svelte"

    import { seasoningsId } from "../../stores/store"

    const seasoningQuery = operationStore<AllSeasonings>(`
        query {
            allSeasonings {
                id
                price
                name
            }
        }
    `)

    query(seasoningQuery);

</script>

<div class="w-full flex flex-col items-center">
    <h1>Select your Seasonings</h1>
    {#if $seasoningQuery.fetching}
        <span>loading</span>
    {:else if $seasoningQuery.error}
        <span>data fetching failed</span>
    {:else}
        <div class="flex flex-row flex-wrap justify-center gap-x-4 gap-y-6 mt-4 mb-2">
        {#each $seasoningQuery.data.allSeasonings as seasoning}
            <MultiCard
                id={seasoning.id}
                name={seasoning.name}
                price={seasoning.price}
                writableIds={seasoningsId}
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