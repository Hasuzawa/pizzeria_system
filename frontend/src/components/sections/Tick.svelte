<script lang="ts">
    import { draw, fade, TransitionConfig } from "svelte/transition"
    import type { CheckboxMode } from "../../types/type"

    export let ticked: boolean = false;
    export let checkboxMode: CheckboxMode;

    const drawConfig: TransitionConfig = {
        duration: 500,
    }

    const fadeConfig: TransitionConfig = {
        duration: 300
    }
    
</script>

<svg
    class="absolute col-start-2 col-span-1 self-end"
    width="46" height="50" viewBox="0 0 46 50" fill="none" xmlns="http://www.w3.org/2000/svg"
>
    {#if checkboxMode === "round"}
        <circle cx="23" cy="34" r="13.5" fill="white" stroke="black" stroke-width="4"/>
    {:else if checkboxMode === "square"}
        <rect x="10.5" y="21.5" width="25" height="25" fill="white" stroke="black" stroke-width="4"/>
    {/if}
    {#if ticked}
        <path
            in:draw={drawConfig}
            out:fade={fadeConfig}
            d="M11 24L23 40L42 9" stroke="#FF0000" stroke-width="6" stroke-linecap="round"
        />
    {/if}
</svg>
    