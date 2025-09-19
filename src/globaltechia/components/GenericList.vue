<template>
  <GenericView>
    <template #header>
      <slot name="header">
        <h2 class="text-center">
          {{ toCapital(name) }}
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
        <GenericTable to="edit" :app="$route.params.app" :view="$route.params.view" selectable="true" :query_params="query_params" @loaded="onLoaded"/>
      </slot>
    </template>
  </GenericView>

</template>

<script setup>

import GenericView from "@/globaltechia/components/GenericView.vue";
import {toCapital} from "@/globaltechia/utils.ts";
import CreateButton from "@/globaltechia/components/buttons/CreateButton.vue";
import {ref} from "vue";
import GenericTable from "@/globaltechia/components/GenericTable.vue";

const props = defineProps(['app','view']);
const query_params = window.location.search;
const name = ref('');

const onLoaded = (val) => {
  name.value = val.value;
}
</script>

<style scoped>

</style>
