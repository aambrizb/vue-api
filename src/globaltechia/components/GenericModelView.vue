<template>
  <GenericView>
    <template #header>
      <h2 class="text-center">
        {{ toCapital(name) }}
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
      <Actions @delete="btnDelete()" @save="btnSave()" :show_delete="$route.params.id ? true:false" />
    </template>
  </GenericView>
</template>

<script setup>

import {watch, ref, onMounted} from "vue";
import GenericView from "@/globaltechia/components/GenericView.vue";
import VueForm from "@/globaltechia/components/GenericForm.vue";
import {useRoute, useRouter} from 'vue-router'
import {getForm, getFullURI, HttpRequest, removeModel, toCapital} from "../utils.ts";
import Actions from "@/globaltechia/components/buttons/Actions.vue";
import Swal from "sweetalert2";

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

const btnSave = () => {
  let is_valid = form.value?.is_valid();
  let data = form.value?.data();
  let full_uri = getFullURI(route.params.app,route.params.view,route.params.id);

  if (is_valid) {

    HttpRequest("POST",full_uri,data)
        .then((data_json) => data_json.json())
        .then((data) => {
          Swal.fire("Operación realizada con éxito", "", "success");
          setTimeout(function() {
            router.replace({ name: 'list', params: { app: route.params.app,view:route.params.view } });
          },800);

        });

  }

};

const btnDelete = () => {
  Swal.fire({
      title: "¿Realmente desea eliminar este elemento?",
      showDenyButton: true,
      confirmButtonText: "Si",
      denyButtonText: `No`
    }).then((result) => {

      if (result.isConfirmed) {
        removeModel(route.params.app, route.params.view, route.params.id).then((ev) => ev.json()).then((data) => {
          Swal.fire(data.msg, "", "success").then(() => {
            router.replace({ name: 'list', params: { app: route.params.app,view:route.params.view } });
          });
        });
      }
  });
}

</script>

<style scoped>

</style>
