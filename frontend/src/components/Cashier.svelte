<script lang="ts">
    import { shapeName, sauceName, toppingsId, seasoningsId } from "../stores/store"
    import { fly, fade, TransitionConfig } from "svelte/transition"

    let price: number = 0;
    
    // note, if you use transition: and not in:, for a brief moment both the unmounting and mounting elements
    // will be visible
    const itemConfig: TransitionConfig = {
        duration: 300
    }

</script>


<div class="h-full flex flex-row items-center">
    
    <div class="w-40 flex flex-row flex-nowrap">
        <span class="mr-2">Shape:</span>
        {#key $shapeName}
        <span class="truncate" in:fade={itemConfig} >
            {$shapeName}
        </span>
        {/key}
    </div>
    <div class="w-40 flex flex-row flex-nowrap">
        <span class="mr-2">Sauce:</span>
        {#key $sauceName}
        <span class="truncate" in:fade={itemConfig} >
            {$sauceName}
        </span>
        {/key}
    </div>
    <div class="w-32 flex flex-row flex-nowrap">
        <span class="mr-2">Toppings:</span>
        {#key $toppingsId}
        <span class="truncate" in:fade={itemConfig} >
            {$toppingsId.length}
        </span>
        {/key}
    </div>
    <div class="w-32 flex flex-row flex-nowrap">
        <span class="mr-2">Seasonings:</span>
        {#key $seasoningsId}
        <span class="truncate" in:fade={itemConfig} >
            {$seasoningsId.length}
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