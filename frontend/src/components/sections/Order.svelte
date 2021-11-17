<script lang="ts">
    import { shapeId, sauceId, toppingsId, seasoningsId, clientName } from "../../stores/store"
    import { ExecuteMutation, mutation } from "@urql/svelte"

    let disabled: boolean = true;

    $: if ($shapeId && $sauceId && $clientName ) {
        disabled = false;
    } else {
        disabled = true;
    }

    const handleClick = () => {
        pizzaMutation({
            clientName: $clientName,
            shapeId: $shapeId,
            sauceId: $sauceId,
            toppingsId: $toppingsId,
            seasoningsId: $seasoningsId
        }).then(x => console.log(x))
    }

    const pizzaMutation = mutation({
        query: `
            mutation ($shapeId: ID!, $sauceId: ID!, $toppingsId: [ID]!, $seasoningsID: [ID]!, $clientName: String!){
                createPizza(client: $clientName, shape: $shapeId, sauce: $sauceId, toppings: $toppingsId, seasonings: $seasoningsID) {
                    pizza{
                        price
                        shape {
                            id
                            name
                        }
                        sauce {
                            id
                            name
                        }
                    }
                }
            }
        `
    })




</script>


<div class="w-full flex flex-col items-center mb-32">
    <button
        class="w-32 h-14 bg-blue-300 rounded-xl"
        disabled={disabled}
        on:click={() => handleClick()}
        class:disabled={disabled}
    >
        Order
    </button>
</div>


<style lang="postcss">

    button {
        font-size: 30px;
    }
    button.disabled {
        background-color: red;
    }
</style>