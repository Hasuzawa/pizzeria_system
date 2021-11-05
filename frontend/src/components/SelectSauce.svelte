<script lang="ts">
    import type { AllSauces } from "src/types/type"
    import { operationStore, query } from "@urql/svelte"
    import Card from "./Card.svelte"

    const sauceQuery = operationStore<AllSauces>(`
        query {
            allSauces {
                name
            }
        }
    `)

    query(sauceQuery);



</script>

<div>
    <h1>Select a sauce</h1>
    {#if $sauceQuery.fetching}
        <span>loading</span>
    {:else if $sauceQuery.error}
        <span>data fetching failed</span>
    {:else}
        <div class="flex flex-row">
        {#each $sauceQuery.data.allSauces as sauce}
            <Card name={sauce.name} />
        {/each}
        </div>
{/if}
</div>

<style lang="postcss">

</style>