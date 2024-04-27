<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

const selectedDate = ref(null);
const formattedDate = computed(() => {
  if (selectedDate.value) {
    const date = new Date(selectedDate.value);
    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();
    return `${day}/${month}/${year}`;
  }
  return '';
});

function postLembrete(){
    
}

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
    <div class="lembrete-form">
        <form action="">
            <fieldset>
                <legend>Lembrete</legend>

                <label for="">Nome</label>
                <input type="text" class="input-field" name='nome-lembrete' required/>

                <div>
                    <label for="">Data</label>
                     <datepicker class="datepicker" v-model="selectedDate" :enable-time-picker="false"/>
                </div>

                <input type="submit" value="Submit" />
            </fieldset>
        </form>
    </div>
</template>

<style scoped>

.lembrete-form{
	max-width: 250px;
	font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
}
.lembrete-form label{
	display:block;
	margin-top: 0.6rem;
}
.lembrete-form {
	color: #F072A9;
	font-weight: bold;
	font-size: 1rem;
	text-shadow: 1px 1px 1px #fff;
}
.lembrete-form fieldset{
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
.lembrete-form fieldset legend{
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
	-moz-box-shadow:-0px -1px 2px #F1F1F1;
	-webkit-box-shadow:-0px -1px 2px #F1F1F1;
	font-weight: normal;
	font-size: 1.3rem;
}
.lembrete-form{
	width:500px;
	height:100px;
    padding-top: 0px;
}
.lembrete-form input[type=text]{
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
	width:100%;
    display:block;
}

.lembrete-form input[type=text]:hover {
    border-color: #C94A81;
}


.lembrete-form  input[type=submit],
.lembrete-form  input[type=button]{
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


.required{
	color:red;
	font-weight:normal;
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
    --dp-disabled-color: #f6f6f6;
    --dp-scroll-bar-background: #f3f3f3;
    --dp-scroll-bar-color: #959595;
    --dp-success-color: #76d275;
    --dp-success-color-disabled: #a3d9b1;
    --dp-icon-color: #C94A81;
    --dp-danger-color: #ff6f60;
    --dp-marker-color: #ff6f60;
    --dp-tooltip-color: #fafafa;
    --dp-disabled-color-text: #8e8e8e;
    --dp-highlight-color: rgb(25 118 210 / 10%);
    --dp-range-between-dates-background-color: var(--dp-hover-color, #f3f3f3);
    --dp-range-between-dates-text-color: var(--dp-hover-text-color, #212121);
    --dp-range-between-border-color: var(--dp-hover-color, #f3f3f3);
}

.datepicker {
    width:100%;
    background-color: #FFCBE2;
}

.datepicker input::placeholder {
    color: #C94A81;
}
.dp__input {
  border-radius: 3px;
  font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
}

  
</style>