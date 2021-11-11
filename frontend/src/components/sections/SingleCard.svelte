<script lang="ts">
    type T = string;
    type U = string;

    import Tick from "./Tick.svelte"
    import type { Writable } from "svelte/store"
    import { fly } from "svelte/transition"

    export let id: string;
    export let name: string;
    export let price: number = 0;
    export let writable_id: Writable<T>;
    export let writable_name: Writable<U>;
    

    let writable_value: T;
    
    writable_id.subscribe((x: T) => {
        writable_value = x
    })

    function writeId(x: T) {
        writable_id.set(x)
    }
    function writeName(x: U) {
        writable_name.set(x)
    }
    const handleInteract = () => {
        writeId(selected ? "" : id)
        writeName(selected ? "" : name)
    }

    const handleClick = (e: MouseEvent) => {
        handleInteract()
    }

    const handleKeyDown = (e: KeyboardEvent) => {
        switch( e.key ){
            case "Enter" : handleInteract(); break;
            default: break;
        }
    }

    let hovered: boolean = false;
    let focused: boolean = false;
    let selected: boolean = false;

    $: selected = (id === writable_value);

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
        <Tick ticked={selected}></Tick>
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