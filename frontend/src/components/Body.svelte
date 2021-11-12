<script lang="ts">
    import SelectShape from "./sections/SelectShape.svelte"
    import SelectSauce from "./sections/SelectSauce.svelte"
    import SelectToppings from "./sections/SelectToppings.svelte"
    import SelectSeasonings from "./sections/SelectSeasonings.svelte"
    import NameInput from "./sections/NameInput.svelte"
    import Send from "./sections/Send.svelte"
</script>


<div id="body" class="flex justify-center">
    <div id="bound" class="max-w-screen-lg flex flex-col items-center gap-y-8">
        <!-- <h1>Choose your Pizza</h1> -->
        <SelectShape />
        <SelectSauce />
        <SelectToppings />
        <SelectSeasonings />
        <NameInput />
        <Send />
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