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
import { useRoute } from 'vue-router'
import {HttpRequest, toCapital} from "../utils.js";

const route = useRoute()

const form  = ref(null);

onMounted(() => {
  loadForm();
});

watch(
  () => route.params.view,
  (newVal, oldVal) => {
    loadForm();
});

const loadForm = () => {
  HttpRequest("GET",route.params.app,route.params.view)
    .then((data) => {
      items.value = data;
  });
};

const items = {
  nombre: {
     type        : 'text',
     name        : 'nombre',
     label       : 'Nombre',
     help_text   : 'Por favor ingrese su nombre completo',
     required    : true,
     error       : null,
     value       : null,
     disabled    : false,
     klass       : 'form-control',
     label_class : 'col-lg-1 col-md-3 col-sm-3 col-xs-12',
     input_class : 'col-lg-11 col-md-9 col-sm-9 col-xs-12'
  },
  paterno:{
     type        : 'text',
     name        : 'paterno',
     label       : 'Paterno',
     help_text   : 'Apellido Paterno',
     required    : true,
     error       : null,
     value       : null,
     disabled    : false,
     klass       : 'form-control',
     label_class : 'col-lg-1 col-md-3 col-sm-3 col-xs-12',
     input_class : 'col-lg-11 col-md-9 col-sm-9 col-xs-12'
  },
  materno:{
     type        : 'text',
     name        : 'materno',
     label       : 'Materno',
     help_text   : 'Apellido Materno',
     required    : true,
     error       : null,
     value       : null,
     disabled    : false,
     klass       : 'form-control',
     label_class : 'col-lg-1 col-md-3 col-sm-3 col-xs-12',
     input_class : 'col-lg-11 col-md-9 col-sm-9 col-xs-12'
  },
  email:{
     type        : 'text',
     name        : 'email',
     label       : 'Email',
     help_text   : 'Email',
     required    : true,
     error       : null,
     value       : null,
     disabled    : false,
     klass       : 'form-control',
     label_class : 'col-lg-1 col-md-3 col-sm-3 col-xs-12',
     input_class : 'col-lg-11 col-md-9 col-sm-9 col-xs-12'
  },
  sexo:{
     type        : 'select',
     name        : 'sexo',
     label       : 'Sexo',
     help_text   : null,
     required    : true,
     error       : null,
     value       : null,
     disabled    : false,
     klass       : 'form-control',
     label_class : 'col-lg-1 col-md-3 col-sm-3 col-xs-12',
     input_class : 'col-lg-11 col-md-9 col-sm-9 col-xs-12',
     choices     : [
       {
         value:'M',
         label:'Masculino'
       },
       {
         value:'F',
         label:'Femenino'
       }
     ]
  },
  password:{
     type        : 'password',
     name        : 'passwd',
     label       : 'Password',
     help_text   : null,
     required    : true,
     error       : null,
     value       : null,
     disabled    : false,
     klass       : 'form-control',
     label_class : 'col-lg-1 col-md-3 col-sm-3 col-xs-12',
     input_class : 'col-lg-11 col-md-9 col-sm-9 col-xs-12'
  },
  observacion:{
     type        : 'textarea',
     name        : 'observacion',
     label       : 'Observaciones',
     help_text   : null,
     required    : true,
     error       : null,
     value       : null,
     disabled    : false,
     klass       : 'form-control',
     label_class : 'col-lg-12 col-md-12 col-sm-12 col-xs-12',
     input_class : 'col-lg-12 col-md-12 col-sm-12 col-xs-12'
  }

};

const save = () => {
  let is_valid = form.value?.is_valid();
  let data = form.value?.data();

  if (is_valid) {
    fetch('http://localhost:8000/api/'+route.params.app+"/"+route.params.view+"/save",{
      method:'POST',
      headers:{
        'Content-Type':'application/json'
      }
    }).then((ev) => {
      console.log(ev);
    });
  }

};

</script>

<style scoped>

</style>
