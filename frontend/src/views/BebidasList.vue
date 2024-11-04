<template>
    <div>
        <h1>Lista de Bebidas</h1>
        <ul>
            <li v-for="bebida in bebidas" :key="bebida.id">{{ bebida.nombre }}</li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            bebidas: []
        };
    },
    created() {
        axios.get('/bebidas/?format=json')
            .then(response => {
                this.bebidas = response.data;
                console.log(this.bebidas[0].bebida)
            })
            .catch(error => {
                console.error("Hubo un error al obtener las bebidas:", error);
            });
    }
};
</script>
