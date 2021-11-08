<script lang="ts">
    import Cashier from "./Cashier.svelte"

</script>

<div id="header" class="flex justify-center justify-items-stretch">
    <div id="bound" class="max-w-screen-lg h-12 flex flex-row justify-between">
        <span>Pizzeria</span>
        <Cashier />
    </div>
</div>

<style lang="postcss">
    #header {
        background-color: #FFAC4B;
    }
    #bound {
        flex: 1 1 0;
        //background-color: lightblue;
    }
</style>

