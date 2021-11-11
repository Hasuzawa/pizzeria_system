<script lang="ts">
    import type { AllShapes } from "src/types/type"
    import { operationStore, query } from "@urql/svelte"
    import SingleCard from "./SingleCard.svelte"

    import { shape_id } from "../../stores/store"

    // backtick `, not single quotation ' !
    const shapeQuery = operationStore<AllShapes>(`
        query {
            allShapes {
                id
                name
            }
        }
    `)

    query(shapeQuery);


</script>


<div class="flex flex-col items-center">
    <h1>Pick a Shape</h1>
    {#if $shapeQuery.fetching}
        <span>loading</span>
    {:else if $shapeQuery.error}
        <span>data fetching failed</span>
    {:else}
        <div class="flex flex-row gap-x-4 mt-4 mb-2">
        {#each $shapeQuery.data.allShapes as shape}
            <SingleCard id={shape.id} name={shape.name} writable={shape_id}/>
        {/each}
        </div>
    {/if}
</div>


<style lang="postcss">
    h1 {
        font-size: 30px;
    }
</style>