<script>
    import { shape, sauce, toppings, seasonings } from "../stores/store"

</script>

<div id="header" class="flex justify-center justify-items-stretch">
    <div id="bound" class="max-w-screen-lg h-12">
        <span>This is header</span>
        <span>Shape: {$shape}</span>
        <span>Sauce: {$sauce}</span>
        <span>{$toppings.length} Toppings</span>
        <span>{$seasonings.length} Seasonings</span>
        <span>Price: </span>
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

