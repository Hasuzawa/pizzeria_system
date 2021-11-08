<script lang="ts">
    import SelectShape from "./sections/SelectShape.svelte"
    import SelectSauce from "./sections/SelectSauce.svelte"
    import SelectToppings from "./sections/SelectToppings.svelte"
    import SelectSeasonings from "./sections/SelectSeasonings.svelte"
</script>


<div id="body" class="flex justify-center">
    <div id="bound" class="max-w-screen-lg flex flex-col items-center">
        <!-- <h1>Choose your Pizza</h1> -->
        <SelectShape />
        <SelectSauce />
        <!-- <SelectToppings /> -->
        <!-- <SelectSeasonings /> -->
    </div> 
</div>


<style lang="postcss">
    h1 {

        font-size: 30px;
    }
    #body {
        background-color: #D13636;
    }
    #bound {
        flex: 1 1 0;
    }
</style>