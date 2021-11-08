<script lang="ts">
    import { draw } from "svelte/transition"
    export let ticked: boolean = false;
</script>

<svg
    class="absolute col-start-2 col-span-1 self-end"
    width="46" height="50" viewBox="0 0 46 50" fill="none" xmlns="http://www.w3.org/2000/svg"
>
    <circle cx="18" cy="34" r="13.5" fill="white" stroke="black" stroke-width="5"/>
    {#if ticked}
        <path d="M4 20.5L18.5 36.5L41.5 4" stroke="#FF0000" stroke-width="8" stroke-linecap="round"/>
    {/if}
</svg>
    