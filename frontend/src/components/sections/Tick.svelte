<script lang="ts">
    import { draw, fade, TransitionConfig } from "svelte/transition"
    export let ticked: boolean = false;

    const drawConfig: TransitionConfig = {
        duration: 500,
    }

    const fadeConfig: TransitionConfig = {
        duration: 300
    }
    //d="M4 20.5L18.5 36.5L41.5 4" stroke="#FF0000" stroke-width="8" stroke-linecap="round"
</script>

<svg
    class="absolute col-start-2 col-span-1 self-end"
    width="46" height="50" viewBox="0 0 46 50" fill="none" xmlns="http://www.w3.org/2000/svg"
>
    <circle cx="23" cy="34" r="13.5" fill="white" stroke="black" stroke-width="4"/>
    {#if ticked}
        <path
            in:draw={drawConfig}
            out:fade={fadeConfig}
            d="M11 24L23 40L42 9" stroke="#FF0000" stroke-width="6" stroke-linecap="round"
        />
    {/if}
</svg>
    