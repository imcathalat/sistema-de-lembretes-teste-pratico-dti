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
    <h1>Novo Lembrete</h1>
    <form action="POST">
        <input type="text" placeholder="Nome do lembrete">
        <input type="date">

        <button type="submit">Enviar</button>
    </form>
</template>