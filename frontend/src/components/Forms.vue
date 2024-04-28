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

function excluirLembrete(idLembrete) {
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
    <div class="max-w-lg mx-auto">
        <div class="shadow-md rounded-md p-6 mb-6 lembrete-form">
            <form v-on:submit.prevent="postLembrete" method="post">
                <fieldset>
                    <legend>Lembrete</legend>

                    <label for="">Nome</label>
                    <input type="text" v-model="name" class="input-field" required />

                    <label for="">Data</label>
                    <input type="date" v-model="date" class="input-field" required />


                    <input type="submit" value="Submit" />
                </fieldset>
            </form>
        </div>
        <div class="shadow-md rounded-md p-6 lembretes">
            <ul class="list-[square] text-pink-500">
                <li v-for="(array, chave) in Object.keys(lembretesPorData).sort((a, b) => new Date(a) - new Date(b))" :key="chave">
                        {{ array }}
                    <ul>
                        <li v-for="lembrete in lembretesPorData[array]" v-bind:key="lembrete.lembrete_id">
                            {{ lembrete.nome }}
                            <button @click="excluirLembrete(lembrete.lembrete_id)">Excluir</button>
                        </li>
                    </ul>
                </li>
            </ul>
        </div>

    </div>
</template>

<style scoped>
.lembrete-form label {
    display: block;
    margin-top: 0.6rem;
}

.lembrete-form {
    font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
    display: block;
    color: #F072A9;
    font-weight: bold;
    font-size: 1rem;
    text-shadow: 1px 1px 1px #fff;
}

.lembrete-form fieldset {
    border-radius: 10px;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    margin: 0px 0px 10px 0px;
    border: 1px solid #FFD2D2;
    padding: 20px;
    background: #FFF4F4;
    box-shadow: inset 0px 0px 15px #FFE5E5;
    -moz-box-shadow: inset 0px 0px 15px #FFE5E5;
    -webkit-box-shadow: inset 0px 0px 15px #FFE5E5;
}

.lembrete-form fieldset legend {
    color: #F072A9;
    border-top: 1px solid #FFD2D2;
    border-left: 1px solid #FFD2D2;
    border-right: 1px solid #FFD2D2;
    border-radius: 5px 5px 0px 0px;
    -webkit-border-radius: 5px 5px 0px 0px;
    -moz-border-radius: 5px 5px 0px 0px;
    background: #FFF4F4;
    padding: 0px 8px 3px 8px;
    box-shadow: -0px -1px 2px #F1F1F1;
    -moz-box-shadow: -0px -1px 2px #F1F1F1;
    -webkit-box-shadow: -0px -1px 2px #F1F1F1;
    font-weight: normal;
    font-size: 1.3rem;
}

.lembrete-form input[type=text],
.lembrete-form input[type=date] {
    border-radius: 3px;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border: 1px solid #FFC2DC;
    outline: none;
    color: #F072A9;
    padding: 6px 30px 6px 12px;
    box-shadow: inset 1px 1px 4px #FFD5E7;
    -moz-box-shadow: inset 1px 1px 4px #FFD5E7;
    -webkit-box-shadow: inset 1px 1px 4px #FFD5E7;
    background: #FFEFF6;
    width: 100%;
    display: block;
}

.lembrete-form input[type=text]:hover {
    border-color: #C94A81;
}


.lembrete-form input[type=submit],
.lembrete-form input[type=button] {
    background: #EB3B88;
    border: 1px solid #C94A81;
    padding: 5px 15px;
    color: #FFCBE2;
    box-shadow: inset -1px -1px 3px #FF62A7;
    -moz-box-shadow: inset -1px -1px 3px #FF62A7;
    -webkit-box-shadow: inset -1px -1px 3px #FF62A7;
    border-radius: 3px;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    font-weight: bold;
    margin: 8% auto 0 auto;
}


.required {
    color: red;
    font-weight: normal;
}

input ::placeholder {
    color: #C94A81;
}

.dp__theme_light {
    --dp-background-color: #FFEFF6;
    --dp-text-color: #C94A81;
    --dp-hover-color: #f3f3f3;
    --dp-hover-text-color: #212121;
    --dp-hover-icon-color: #959595;
    --dp-primary-color: #C94A81;
    --dp-primary-disabled-color: #6bacea;
    --dp-primary-text-color: #f8f5f5;
    --dp-secondary-color: #c0c4cc;
    --dp-border-color: #FFC2DC;
    --dp-menu-border-color: #ddd;
    --dp-border-color-hover: #C94A81;
    --dp-disabled-color: #C94A81;
    --dp-scroll-bar-background: #f3f3f3;
    --dp-scroll-bar-color: #959595;
    --dp-success-color: #76d275;
    --dp-success-color-disabled: #a3d9b1;
    --dp-icon-color: #C94A81;
    --dp-danger-color: #ff6f60;
    --dp-marker-color: #ff6f60;
    --dp-tooltip-color: #C94A81;
    --dp-disabled-color-text: #8e8e8e;
    --dp-highlight-color: rgb(25 118 210 / 10%);
    --dp-range-between-dates-background-color: var(--dp-hover-color, #f3f3f3);
    --dp-range-between-dates-text-color: var(--dp-hover-text-color, #212121);
    --dp-range-between-border-color: var(--dp-hover-color, #f3f3f3);
}

.datepicker {
    width: 100%;
    background-color: #FFCBE2;
}

.datepicker input::placeholder {
    color: #C94A81;
}

.dp__input {
    border-radius: 3px;
    font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
}


.lembretes {
    display: block;
}
</style>