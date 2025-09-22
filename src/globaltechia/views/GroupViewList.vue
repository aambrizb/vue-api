<template>
  <GenericList>
    <template #header>
      <h1 class="text-center">
        Grupos
      </h1>
    </template>
    <template #top_button>
      <div class="align-middle">
        <CreateButton to="create_group" app="base" view="Group" />
      </div>
    </template>
    <template #body>
      <GenericTable to="edit_group" app="base" view="Group" selectable="true" :query_params="query_params"/>
    </template>
  </GenericList>
</template>

<script setup>
import GenericList from "../components/GenericList.vue";
import CreateButton from "../components/buttons/CreateButton.vue";
import GenericTable from "../components/GenericTable.vue";

const query_params = window.location.search;

</script>

<style scoped>

</style>
