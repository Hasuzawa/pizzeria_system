<script lang="ts">
    import type { AllSeasonings } from "src/types/type";
    import { operationStore, query } from "@urql/svelte"
    import Card from "./Card.svelte"

    const seasoningQuery = operationStore<AllSeasonings>(`
        query {
            allSeasonings {
                price
                name
            }
        }
    `)

    query(seasoningQuery);

</script>

<div>
    <h1>Select your Seasonings</h1>
    {#if $seasoningQuery.fetching}
        <span>loading</span>
    {:else if $seasoningQuery.error}
        <span>data fetching failed</span>
    {:else}
        <div class="flex flex-row">
        {#each $seasoningQuery.data.allSeasonings as seasoning}
            <Card name={seasoning.name} />
        {/each}
        </div>
    {/if}
</div>