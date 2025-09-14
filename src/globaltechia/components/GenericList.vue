<template>
  <GenericView>
    <template #header>
      <slot name="header">
        <h2 class="text-center">
          {{ toCapital($route.params.view) }}
        </h2>
      </slot>
    </template>
    <template #top_button>
      <slot name="top_button">
        <CreateButton to="create" :app="$route.params.app" :view="$route.params.view" />
      </slot>
    </template>
    <template #body>
      <slot name="body">
        <Tabla :app="$route.params.app" :view="$route.params.view" selectable="true" :query_params="query_params" />
      </slot>
    </template>
  </GenericView>

</template>

<script setup>

import Tabla from "@/globaltechia/components/Tabla.vue";
import GenericView from "@/globaltechia/components/GenericView.vue";
import {toCapital} from "@/globaltechia/utils.ts";
import CreateButton from "@/globaltechia/components/buttons/CreateButton.vue";

const props = defineProps(['app','view']);
const query_params = window.location.search;
</script>

<style scoped>

</style>
