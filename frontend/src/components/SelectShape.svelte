<script lang="ts">
    import type { AllShapes } from "src/types/type"
    import { operationStore, query } from "@urql/svelte"
    import Card from "./Card.svelte"

    // backtick `, not single quotation ' !
    const shapeQuery = operationStore<AllShapes>(`
        query {
            allShapes {
                name
            }
        }
    `)

    query(shapeQuery)

</script>

<div>
    <h1>Pick a Shape</h1>
    {#if $shapeQuery.fetching}
        <span>loading</span>
    {:else if $shapeQuery.error}
        <span>data fetching failed</span>
    {:else}
        <div class="flex flex-row">
        {#each $shapeQuery.data.allShapes as shape}
            <Card name={shape.name} />
        {/each}
        </div>
    {/if}
</div>

<style lang="postcss">

</style>