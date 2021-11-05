<script context="module">
    export let selected;
</script>

<script lang="ts">
    export let name: string;
</script>

<!-- round corner!, when focused, glow ring, hover then card move upward a bit   -->
<div class="flex-0 w-40 h-48 rounded-xl bg-black text-white  flex flex-col items-center">
    <div class="h-40">

    </div>
    <h1>{name}</h1>
</div>