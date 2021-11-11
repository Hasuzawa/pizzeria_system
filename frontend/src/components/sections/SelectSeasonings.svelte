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

<div class="flex flex-col items-center">
    <h1>Select your Seasonings</h1>
    {#if $seasoningQuery.fetching}
        <span>loading</span>
    {:else if $seasoningQuery.error}
        <span>data fetching failed</span>
    {:else}
        <div class="flex flex-row">
        {#each $seasoningQuery.data.allSeasonings as seasoning}
            <MultiCard
                id={seasoning.id}
                name={seasoning.name}
                price={seasoning.price}
                writableId={seasoningsId}
            />
        {/each}
        </div>
    {/if}
</div>