<template>
  <GenericList>
    <template #header>
      <h1 class="text-center">
        Usuarios
      </h1>
    </template>
    <template #top_button>
      <div class="align-middle">
        <CreateButton to="create_user" app="app" view="User" />
      </div>
    </template>
    <template #body>
      <Tabla to="edit_user" app="base" view="User" selectable="true" :query_params="query_params"/>
    </template>
  </GenericList>
</template>

<script setup>
import GenericList from "@/globaltechia/components/GenericList.vue";
import CreateButton from "@/globaltechia/components/buttons/CreateButton.vue";
import Tabla from "@/globaltechia/components/Tabla.vue";

const query_params = window.location.search;

</script>

<style scoped>

</style>