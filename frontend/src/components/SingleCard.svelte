<script context="module" lang="ts">
    
</script>

<script lang="ts">
    type T = string;

    import Tick from "./Tick.svelte"
    import type { Writable } from "svelte/store"

    export let name: string;
    export let price: number = 0;
    export let writable: Writable<T>;

    let writable_value: T;
    
    writable.subscribe((x: T) => {
        writable_value = x
    })

    function setWritable(x: T) {
        writable.set(x);
    }


    let hovered: boolean = false;
    let focused: boolean = false;
    let selected: boolean = false;

    $: selected = (name === writable_value);

</script>

<!-- round corner!, when focused, glow ring, hover then card move upward a bit   -->
<div
    class="flex-0 w-40 h-48 rounded-xl bg-gray-300 text-whi  flex flex-col items-center relative"
    on:click={() => setWritable(name)}
    on:mouseover={() => hovered = true}
    on:mouseout={() => hovered = false}
    on:focus={() => focused = true}
    on:blur={() => focused = false}
    id="single-card"
    tabindex={0}
    class:hovered={hovered}
    class:focused={focused}
    class:selected={selected}
>
    <div class="h-32">

    </div>
    <h1>{name}</h1>
    <div id="card-details" class="w-full h-8 grid grid-cols-3 justify-items-center relative">
        {#if price != 0}
        <price>${price}</price>
        {/if}
        <Tick></Tick>
    </div>
</div>

<style lang="postcss">
    #single-card{
        top: 0;
        transition: top ease-in-out 0.15s;
    }
    #single-card.hovered{
        top: -15px;
    }

    #single-card.focused{
        color: red;
    }

    #single-card.selected{
        color: blue;
    }

    #card-details {

    }
</style>