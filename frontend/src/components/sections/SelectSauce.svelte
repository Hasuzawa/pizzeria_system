<script lang="ts">
    import type { AllSauces } from "src/types/type"
    import { operationStore, query } from "@urql/svelte"
    import SingleCard from "./SingleCard.svelte"

    import { sauceId, sauceName } from "../../stores/store"

    const sauceQuery = operationStore<AllSauces>(`
        query {
            allSauces {
                id
                name
            }
        }
    `)

    query(sauceQuery);

</script>

<div class="flex flex-col items-center">
    <h1>Select a sauce</h1>
    {#if $sauceQuery.fetching}
        <span>loading</span>
    {:else if $sauceQuery.error}
        <span>data fetching failed</span>
    {:else}
        <div class="flex flex-row gap-x-4 mt-4 mb-2">
        {#each $sauceQuery.data.allSauces as sauce}
            <SingleCard id={sauce.id} name={sauce.name} writable_id={sauceId} writable_name={sauceName}/>
        {/each}
        </div>
{/if}
</div>

<style lang="postcss">
    h1 {
        font-size: 30px;
    }
</style>