<template>
  <GenericView :messages="messages">
    <template #header>
      <h1 class="text-center">Reporte de Activaciones</h1>
    </template>
    <template #body>
      <GenericItem :item="items['fecha_inicio']" />
      <GenericItem :item="items['fecha_fin']" />
      <div class="row">
        <div class="col-10"></div>
        <div class="col-2">
          <button type="button" class="btn btn-primary" @click="buscar()">
            <span class="fa fa-search"></span>
            Buscar
          </button>
        </div>
      </div>
    </template>
  </GenericView>

</template>

<script setup>
  import {ref} from "vue";
  import GenericItem from "@/globaltechia/components/GenericItem.vue";
  import GenericView from "@/globaltechia/components/GenericView.vue";

  const messages = ref([]);

  const items = {
    fecha_inicio: {
     type        : 'date',
     name        : 'fecha_inicio',
     label       : 'Fecha de Inicio',
     help_text   : null,
     required    : true,
     error       : null,
     value       : null,
     disabled    : false,
     class       : 'form-control',
     label_class : 'col-lg-2 col-md-2 col-sm-2 col-xs-12',
     input_class : 'col-lg-2 col-md-2 col-sm-2 col-xs-12'
   },
   fecha_fin: {
     type        : 'date',
     name        : 'fecha_fin',
     label       : 'Fecha de Fin',
     help_text   : null,
     required    : true,
     error       : null,
     value       : null,
     disabled    : false,
     class       : 'form-control',
     label_class : 'col-lg-2 col-md-2 col-sm-2 col-xs-12',
     input_class : 'col-lg-2 col-md-2 col-sm-2 col-xs-12'
   }
  };

  const buscar = () => {
    messages.value = [{type:'success',msg:'Reporte generado con éxito'}];
  };

</script>

<style scoped>

</style>
