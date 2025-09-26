<template>
<GenericModalView>
  <template #modal_title>
    {{ modal_title }}
  </template>
  <template #modal_body>
    <GenericForm :items="items" />
  </template>
  <template #modal_footer>
    <button type="button" class="btn btn-primary" @click="btnSave">
      <span class="fa fa-save"></span>
      Guardar
    </button>
  </template>
</GenericModalView>
</template>

<script setup>
import GenericModalView from "../components/GenericModalView.vue";
import GenericForm from "../components/GenericForm.vue";
import {
  getForm,
  getFormData,
  RemoveModal,
  addModel
} from "../utils";

import {onMounted, ref} from "vue";

const props   = defineProps(['title','app','view','pk','extra'])

const modal_title = ref(null);
const loading     = ref(false);
const items       = ref(null);
const name        = ref(null);

onMounted(() => {

  modal_title.value = props.title

  getForm(props.app,props.view,props.pk).then((data) => {
    name.value    = data.verbose_name;
    items.value   = data.form;
    loading.value = false;
  });
});

const btnSave = () => {

  let params = getFormData(items.value);
  const final_params = Object.assign({},params,props.extra);

  addModel(props.app,props.view,final_params).then((data_json) => data_json.json()).then((data) => {
    if (data.code === 200) {

       RemoveModal();

       const event = new CustomEvent("AddModel", {
         detail: {
           app: props.app,
           view: props.view,
           id: props.pk
         },
       });

      document.dispatchEvent(event);

    }
  });
};

</script>

<style scoped>

</style>
