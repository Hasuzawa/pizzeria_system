<script lang="ts">
    type T = string;
    import type { Writable } from "svelte/store"
    import Card from "./Card.svelte"

    export let id: string;
    export let name: string;
    export let price: number;
    export let writableId: Writable<String[]>;

    export let minTopping: number = 0;
    export let maxTopping: number = 10;

    let selectedIds: string[] = [];



    const handleClick = () => {

    }

    const handleInteract = () => {

    }

    const handleKeyDown = (e: KeyboardEvent) => {
        switch( e.key ){
            case "Enter" : handleInteract(); break;
            default: break;
        }
    }


</script>


