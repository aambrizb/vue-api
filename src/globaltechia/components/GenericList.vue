<template>
  <GenericView>
    <template #header>
      <h2 class="text-center">
        {{ toCapital($route.params.view) }}
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
import GenericView from "@/globaltechia/components/GenericView.vue";
import {toCapital} from "@/globaltechia/utils.js";

const props = defineProps(['app','view']);

</script>

<style scoped>

</style>
