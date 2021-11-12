<script lang="ts">
    import { clientName } from "../../stores/store"
    


</script>


<div class="w-full flex flex-col items-center">
    <h1>How may you be addressed?</h1>
    <h2>*Since this a just a demo, this will not be used for anything*</h2>
    <input
        bind:value={$clientName}
        spellcheck={false}
        class="w-60 h-8 rounded mt-4"
    >
</div>


<style lang="postcss">
    h1 {
        font-size: 30px;
    }
    h2 {
        font-size: 20px;
    }
    input {
        font-size: 18px;
    }
</style>