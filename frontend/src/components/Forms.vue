<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'


function getLembretes() {
    axios.get('/lembretes/')
    .then(response => {
        console.log('data', response.data)
    })
    .catch(error => {
        console.log('error', error)
    })
}

function postLembretes(){
    
}

onMounted(() => {
    getLembretes()
})
</script>
<template>
    <h1 class="text-cyan-500 font-bold underline">
        Hello world!
    </h1>
</template>