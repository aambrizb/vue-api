<template>
  <GenericView>
    <template #header>
      <h2 class="text-center">
        {{ toCapital($route.params.view) }}
      </h2>
      <h5 class="text-center text-secondary" v-if="$route.params.id">{{ $route.params.id }}</h5>
    </template>
    <template #top_button>
      <router-link class="btn btn-sm btn-secondary pull-right" :to="{ name: 'list', params: { 'app':$route.params.app,'view': $route.params.view }}">
        <span class="fa fa-list"></span>
        Listar
      </router-link>
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
      <div class="row">
          <div class="col-11"></div>
          <div class="col-1">
            <button class="btn btn-sm btn-primary pull-right" @click="save();">
              <span class="fa fa-save"></span>
              Guardar
            </button>
          </div>
        </div>
    </template>
  </GenericView>
</template>

<script setup>

import {watch, ref, onMounted} from "vue";
import GenericView from "@/globaltechia/components/GenericView.vue";
import VueForm from "@/globaltechia/components/GenericForm.vue";
import {useRoute, useRouter} from 'vue-router'
import {getForm, getFullURI, HttpRequest, toCapital} from "../utils.ts";

const route   = useRoute();
const router  = useRouter()
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
    items.value = data;
    loading.value = false;
  });
};

const save = () => {
  let is_valid = form.value?.is_valid();
  let data = form.value?.data();
  let full_uri = getFullURI(route.params.app,route.params.view,route.params.id);

  if (is_valid) {

    HttpRequest("POST",full_uri,data)
        .then((data_json) => data_json.json())
        .then((data) => {
          router.replace({ name: 'list', params: { app: route.params.app,view:route.params.view } });
        });

  }

};

</script>

<style scoped>

</style>
