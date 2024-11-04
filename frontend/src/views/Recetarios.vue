<template>
	<div class="container">
	  <h1 class="text-center my-4">Recetarios</h1>
	  <div class="row">
		<div class="col-md-4 mb-4" v-for="recetario in recetarios" :key="recetario.id">
		  <div class="card">
			<img :src="getRandomImage()" class="card-img-top" alt="Recetario Imagen">
			<div class="card-body">
			  <h5 class="card-title">{{ recetario.nombre }}</h5>
			  <p class="card-text">{{ recetario.descripcion }}</p>
				<router-link :to="{ name: 'newRecetario', params: { id: recetario.id } }" class="btn btn-primary">Ver Detalles</router-link>
			</div>
		  </div>
		</div>
	  </div>
	</div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
	data() {
	  return {
		recetarios: [],
		images: [
		  'https://termosyeti.com/wp-content/uploads/2023/10/bebidas-alcoholicas.jpg',
		  'https://i0.wp.com/granvita.com/wp-content/uploads/2020/06/acelerar_metabolismo_bebidas_saludables.jpg',
		  'https://media.cnn.com/api/v1/images/stellar/prod/cnne-1363935-las-5-mejores-bebidas-espirituosas-del-mundo-segun-tasteatlas.jpeg',
		  'https://thefoodtech.com/wp-content/uploads/2023/10/bebidas-1-828x548.jpg',
		]
	  };
	},
	created() {
	  this.fetchRecetarios();
	},
	methods: {
	  async fetchRecetarios() {
		try {
		  const response = await axios.get('/recetarios/'); // Asegúrate de que esta URL sea correcta
		  this.recetarios = response.data;
		  console.log(this.recetarios)
		} catch (error) {
		  console.error('Error fetching recetarios:', error);
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
  