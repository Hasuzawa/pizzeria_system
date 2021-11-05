<script lang="ts">
    import type { AllShapes } from "../types/type"
    import { operationStore, query } from "@urql/svelte"

    // backtick `, not single quotation ' !
    const shapeQuery = operationStore<AllShapes>(`
        query {
            allShapes {
                name
            }
        }
    `)

    query(shapeQuery)

    $: if (shapeQuery) console.log(shapeQuery.data)

</script>

<div>

    <h1>Select Shape</h1>
    {#if $shapeQuery.fetching}
        <span>loading</span>
    {:else if $shapeQuery.error}
        <span>data fetching failed</span>
    {:else}
        {#each $shapeQuery.data.allShapes as shape}
            <span>{shape.name}</span>
        {/each}
    {/if}
</div>

<style lang="postcss">

</style>