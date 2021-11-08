<script context="module">
    export let selected;

</script>

<script lang="ts">
    export let name: string;

    let hovered: boolean = false;
    let focused: boolean = false;

    $: console.log("hovered: ", hovered);
    $: console.log("focused: ", focused);

</script>

<!-- round corner!, when focused, glow ring, hover then card move upward a bit   -->
<div
    class="flex-0 w-40 h-48 rounded-xl bg-black text-white  flex flex-col items-center relative"
    on:mouseover={() => hovered = true}
    on:mouseout={() => hovered = false}
    on:focus={() => focused = true}
    on:blur={() => focused = false}
    id="single-card"
    tabindex={0}
    class:hovered={hovered}
    class:focused={focused}
>
    <div class="h-40">

    </div>
    <h1>{name}</h1>
    
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
</style>