<script lang="ts">
    import Tick from "./Tick.svelte"
    import { fly } from "svelte/transition"
    import type { CheckboxMode } from "../../types/type"

    export let handleClick
    export let handleKeyDown

    export let name: string;
    export let price: number;
    export let selected: boolean;

    export let checkboxMode: CheckboxMode;


    let hovered: boolean = false;
    let focused: boolean = false;
</script>


<div
    class="flex-0 w-40 h-48 rounded-xl bg-gray-300 text-whi  flex flex-col items-center relative shadow-2xl"
    on:click={handleClick}
    on:mouseover={() => hovered = true}
    on:mouseout={() => {hovered = false; focused = false}}
    on:focus={() => focused = true}
    on:blur={() => focused = false}
    on:keydown={handleKeyDown}
    id="single-card"
    tabindex={0}
    class:hovered={hovered}
    class:focused={!hovered && focused}
    in:fly={{y: 20}}
>
    <div class="h-32">

    </div>
    <h1>{name}</h1>
    <div id="card-details" class="w-full h-8 grid grid-cols-3 justify-items-center relative">
        {#if price != 0}
        <price>${price}</price>
        {/if}
        <Tick
            ticked={selected}
            {checkboxMode}
        />
    </div>
</div>


<style lang="postcss">
    #single-card{
        top: 0;
        outline: none;
        transition: top ease-in-out 0.15s;
    }
    #single-card.hovered{
        outline: none;
        top: -15px;
    }

    /* normally, focus also works by mouse click, but by using !hovered and focused = false when mouseout,
        this becomes a keyboard-focus only effect */
    #single-card.focused{
        outline: none;  /* disable default focus highlight, remember to implement someways to indicate focus */
        top: -15px;
        outline: solid 4px black;
        box-shadow: 0px 0px 30px 10px #FFAC4B;
    }
</style>