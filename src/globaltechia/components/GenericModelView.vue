<template>
  <GenericView>
    <template #header>
      <h2 class="text-center">
        {{ toCapital(name) }}
      </h2>
      <h5 class="text-center text-secondary" v-if="$route.params.id">{{ $route.params.id }}</h5>
    </template>
    <template #top_button>
      <ListButton to="list" :app="$route.params.app" :view="$route.params.view"/>
    </template>
    <template #body>
      <div class="text-center" v-if="loading">
        <div class="spinner-border " role="status">
          <span class="sr-only">Loading...</span>
        </div>
      </div>
      <VueForm ref="form" :items="items"/>
    </template>
    <template #footer>
      <Actions @delete="btnDelete()" @save="btnSave" :show_delete="$route.params.id ? true:false" />
    </template>
  </GenericView>
</template>

<script setup>

import {watch, ref, onMounted} from "vue";
import GenericView from "./GenericView.vue";
import VueForm from "./GenericForm.vue";
import {useRoute, useRouter} from 'vue-router'
import {getForm, toCapital, DefaultBtnSave, DefaultBtnDelete, ValidateData, getFormData} from "../utils";
import Actions from "./buttons/Actions.vue";
import ListButton from "./buttons/ListButton.vue";

const route   = useRoute();
const router  = useRouter()
const name    = ref('');
const loading = ref(false);
const items   = ref({});
const form    = ref(null);

onMounted(() => {
  loadForm(route.params.app,route.params.view,route.params.id);
});

watch(
  () => route.params.view,
  (newVal, oldVal) => {
    loadForm(route.params.app,route.params.view,route.params.id);
});

const loadForm = () => {
  loading.value = true;
  getForm(route.params.app,route.params.view,route.params.id).then((data) => {
    name.value    = data.verbose_name;
    items.value   = data.form;
    loading.value = false;
  });
};

const btnSave = (ev,extra) => {
  
  let is_valid = ValidateData(items.value);
  let data     = getFormData(items.value);

  if (!is_valid) return;


  DefaultBtnSave(extra,route.params.app,route.params.view,data,route.params.id);

};

const btnDelete = () => {
  DefaultBtnDelete(route.params.app,route.params.view,route.params.id);
}

</script>

<style scoped>

</style>
