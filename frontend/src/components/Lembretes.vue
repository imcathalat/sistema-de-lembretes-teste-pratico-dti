<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const name = ref('');
const date = ref('');

const lembretes = ref([]);
const lembretesPorData = ref([]);

function formatarDataBr(data) {
    const partes = data.split('-');
    const dataFormatada = `${partes[2]}/${partes[1]}/${partes[0]}`;
    return dataFormatada;
}

function agruparLembretesPorData() {
    const groupedLembretes = {};

    lembretes.value.forEach(lembrete => {
        // Verifica se já existe uma entrada para a data atual
        if (!groupedLembretes[lembrete.data]) {
            // Se não existe, cria um novo array para essa data
            groupedLembretes[lembrete.data] = [];
        }

        // Adiciona o lembrete ao array associado à sua data
        groupedLembretes[lembrete.data].push(lembrete);
    });

    lembretesPorData.value = groupedLembretes;

    const chaves = Object.keys(lembretesPorData.value);
}

function getLembretes() {
    axios.get('/lembretes/')
        .then(response => {
            
            lembretes.value = response.data.map(lembrete => ({
                ...lembrete, // cópia do objeto lembrete que esta sendo iterado
                data: formatarDataBr(lembrete.data) // substrituição do atributo data desse objeto que foi copiado
            }));

            console.log("lembretes: ", lembretes.value);

        })
        .then(() => {
            agruparLembretesPorData();
        })
        .catch(error => {
            console.log('error', error)
        })
}

function postLembrete() {
    const nome = name.value;

    const data = new Date(date.value).toISOString().split('T')[0];
    console.log(data);

    console.log({ nome, data })

    axios.post('/lembretes/', { nome, data })
        .then(response => {
            console.log(response.data);
            getLembretes()
            name.value = ''
            date.value = ''
        })
        .catch(error => {
            console.error('Erro: ', error);
        })
}

function deleteLembrete(idLembrete) {
    console.log(idLembrete)
    axios.delete(`/lembretes/${idLembrete}/`)
        .then(response => {
            console.log('Lembrete excluído:', idLembrete);
            getLembretes();
        })
        .catch(error => {
            console.error('Erro ao excluir lembrete:', error);
        })
}

onMounted(() => {
    getLembretes()
})

</script>

<template>
    
    <div class="card">
        <div class=" lembrete-form">
            <form v-on:submit.prevent="postLembrete" method="post">
                <fieldset>
                    <legend>Novo Lembrete</legend>

                    <label for="">Nome</label>
                    <input type="text" v-model="name" class="input-field" required />

                    <label for="">Data</label>
                    <input type="date" v-model="date" class="input-field" required />


                    <input type="submit" value="Submit" />
                </fieldset>
            </form>
        </div>
        <div class=" lembretes">
            <h1 class="title">Lembretes</h1>
            <ul class="list-[square] text-pink-500">
                <li v-for="(array, chave) in Object.keys(lembretesPorData).sort((a, b) => new Date(a) - new Date(b))" :key="chave">
                        <strong>{{ array }}</strong>
                    <ul>
                        <li v-for="lembrete in lembretesPorData[array]" v-bind:key="lembrete.lembrete_id">
                            {{ lembrete.nome }}
                            
                            <button @click="deleteLembrete(lembrete.lembrete_id)"><i class="pi pi-trash"></i></button>
                        </li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</template>

<style lang='scss' scoped>
@import '@/assets/_main.scss';

</style>