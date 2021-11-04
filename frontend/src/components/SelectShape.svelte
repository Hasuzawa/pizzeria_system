<script lang="ts">
    //import { getClient, query } from "svelte-apollo"
    //import { gql } from "@apollo/client/core"
    //import GET_ALL_SHAPES from "../graphql/query.graphql"
    import type { Shape } from "../types/type"

    import { operationStore, query } from "@urql/svelte"

    const shapeQuery = operationStore(`
        query {
            allShapes {
                name
            }
        }
    `)

    query(shapeQuery)

    // backtick `, not single quotation ' !

    // const client = getClient()

    // const shapeQuery = client.query({query: GET_ALL_SHAPES});
    // console.log(shapeQuery);
    //console.log()
    $: if (shapeQuery) console.log(shapeQuery)

</script>

<div>
    <h1>Select Shape</h1>
    <!-- {#each shapeQuery.data.allShapes as shape}
        <span>{shape.name}</span>
    {/each} -->
</div>

<style lang="postcss">

</style>