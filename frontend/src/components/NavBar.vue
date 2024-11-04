<template>
    <div class="container">
        <header class="d-flex justify-content-center py-3">
        <ul class="nav nav-pills">
            <li class="nav-item">
                <router-link class="nav-link active" to="/">Inicio</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/recetarios/">Mis Recetarios</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/bebidas/">Explorar Bebidas</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/recetarios/new/">Crear Recetario</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/bebidas/new">Crear Bebida</router-link>
            </li>
        </ul>
        </header>
    </div>
</template>
