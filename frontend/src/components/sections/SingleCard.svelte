<script lang="ts">
    type T = string;
    type U = string;

    import type { Writable } from "svelte/store"
    import Card from "./Card.svelte";

    export let id: string;
    export let name: string;
    export let price: number = 0;
    export let writableId: Writable<T>;
    export let writableName: Writable<U>;
    

    // let writable_value: T;
    
    // writable_id.subscribe((x: T) => {
    //     //writable_value = x
    // })

    function writeId(x: T) {
        writableId.set(x)
    }
    function writeName(x: U) {
        writableName.set(x)
    }
    const handleInteract = () => {
        writeId(selected ? "" : id)
        writeName(selected ? "" : name)
    }

    const handleClick = (e: MouseEvent) => {
        handleInteract()
    }

    const handleKeyDown = (e: KeyboardEvent) => {
        switch( e.key ){
            case "Enter" : handleInteract(); break;
            default: break;
        }
    }

    let selected: boolean = false;

    $: selected = (id === $writableId);

</script>

<Card
    {handleClick}
    {handleKeyDown}
    {name}
    {price}
    {selected}
/>