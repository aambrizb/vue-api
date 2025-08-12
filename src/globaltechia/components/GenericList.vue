<template>
  <GenericView>
    <template #header>
      <h2 class="text-center">
        {{ $route.params.view }}
      </h2>
    </template>
    <template #top_button>
      <router-link class="btn btn-sm btn-primary pull-right" :to="{ name: 'create', params: { 'app':$route.params.app,'view': $route.params.view }}">
        <span class="fa fa-folder"></span>
        Nuevo
      </router-link>
    </template>
    <template #body>
      <Tabla />
    </template>
  </GenericView>

</template>

<script setup>

import Tabla from "@/globaltechia/components/Tabla.vue";
import VueForm from "@/globaltechia/components/GenericForm.vue";
import GenericView from "@/globaltechia/components/GenericView.vue";

const props = defineProps(['app','view']);

</script>

<style scoped>

</style>
