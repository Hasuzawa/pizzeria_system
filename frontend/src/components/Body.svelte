<script lang="ts">
    import SelectShape from "./SelectShape.svelte"
    import SelectSauce from "./SelectSauce.svelte"
</script>


<div id="body" class="flex justify-center">
    <div id="bound" class="max-w-screen-lg flex flex-col items-center">
        <h1>Choose your Pizza</h1>
        <SelectShape />
        <SelectSauce />
    </div>
</div>


<style lang="postcss">
    #body {
        background-color: #D13636;
    }
    #bound {
        flex: 1 1 0;
        //background-color: lightblue;
    }
</style>