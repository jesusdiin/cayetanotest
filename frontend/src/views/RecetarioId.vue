<!-- src/components/RecetarioDetail.vue -->
<template>
    <div class="container">
      <h1 class="text-center my-4">{{ recetario.nombre }}</h1>
      <div class="card">
        <img :src="getRandomImage()" class="card-img-top" alt="Recetario Imagen">
        <div class="card-body">
          <h5 class="card-title">{{ recetario.nombre }}</h5>
          <p class="card-text">{{ recetario.descripcion }}</p>
        </div>
      </div>
      <router-link to="/recetarios" class="btn btn-secondary mt-3">Regresar</router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        recetario: {},
        images: [
          'https://termosyeti.com/wp-content/uploads/2023/10/bebidas-alcoholicas.jpg',
        ]
      };
    },
    created() {
      this.fetchRecetario();
    },
    methods: {
      async fetchRecetario() {
        const recetarioId = this.$route.params.id;
        console.log(recetarioId)
        try {
          const response = await axios.get(`/recetarios/${recetarioId}/`); // Asegúrate de que esta URL sea correcta
          this.recetario = response.data;
        } catch (error) {
          console.error('Error fetching recetario:', error);
        }
      },
      getRandomImage() {
        const randomIndex = Math.floor(Math.random() * this.images.length);
        return this.images[randomIndex];
      }
    }
  };
  </script>
  
  <style scoped>
  .card {
    transition: transform 0.2s;
  }
  .card:hover {
    transform: scale(1.05);
  }
  </style>
  