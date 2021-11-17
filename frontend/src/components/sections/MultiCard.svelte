<script lang="ts">
    type T = string;
    import type { Writable } from "svelte/store"
    import Card from "./Card.svelte"

    export let id: string;
    export let name: string;
    export let price: number;
    export let writableIds: Writable<String[]>;

    //export let minTopping: number = 0;
    //export let maxTopping: number = 10;

    let selected: boolean;

    //let selectedIds: string[] = [];

    $: selected = $writableIds.includes(id);



    const handleInteract = () => {
        if (selected) {
            $writableIds = $writableIds.filter(x => x != id);
        } else {
            $writableIds = [...$writableIds, id]
        }
    }

    const handleClick = (e: MouseEvent) => {
        handleInteract();
    }

    const handleKeyDown = (e: KeyboardEvent) => {
        switch( e.key ){
            case "Enter" : handleInteract(); break;
            default: break;
        }
    }


</script>


<Card
    {handleClick}
    {handleKeyDown}
    {name}
    {price}
    {selected}
    checkboxMode="square"
/>