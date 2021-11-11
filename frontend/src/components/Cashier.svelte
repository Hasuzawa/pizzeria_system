<script lang="ts">
    import { shape_id, sauce_id, toppings_id, seasonings_id } from "../stores/store"
    import { fly, fade, TransitionConfig } from "svelte/transition"

    let price: number = 0;
    
    // note, if you use transition: and not in:, for a brief moment both the unmounting and mounting elements
    // will be visible
    const itemConfig: TransitionConfig = {
        duration: 300
    }

    let shape: string;
    let sauce: string;
    let toppings: string[];
    let seasonings: string[];

    $: shape = "3"
    $: sauce = "2"
    $: toppings = ["2"]
    $: seasonings = ["5"]

</script>


<div class="h-full flex flex-row items-center">
    
    <div class="w-40 flex flex-row flex-nowrap">
        <span class="mr-2">Shape:</span>
        {#key shape}
        <span class="truncate" in:fade={itemConfig} >
            {shape}
        </span>
        {/key}
    </div>
    <div class="w-40 flex flex-row flex-nowrap">
        <span class="mr-2">Sauce:</span>
        {#key sauce}
        <span class="truncate" in:fade={itemConfig} >
            {sauce}
        </span>
        {/key}
    </div>
    <div class="w-32 flex flex-row flex-nowrap">
        <span class="mr-2">Toppings:</span>
        {#key toppings}
        <span class="truncate" in:fade={itemConfig} >
            {toppings.length}
        </span>
        {/key}
    </div>
    <div class="w-32 flex flex-row flex-nowrap">
        <span class="mr-2">Seasonings:</span>
        {#key seasonings}
        <span class="truncate" in:fade={itemConfig} >
            {seasonings.length}
        </span>
        {/key}
    </div>
    <div class="ml-8">
        <span>$</span>
        {#key price}
        <span in:fly={{y: -20}}>{price}</span>
        {/key}
    </div>
    
</div>


<style lang="postcss">
    div {
        font-size: 20px;
    }
</style>