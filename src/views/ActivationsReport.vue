<template>
  <GenericView :messages="messages">
    <template #header>
      <h1 class="text-center">Reporte de Activaciones</h1>
    </template>
    <template #body>
      <GenericItem :item="items['fecha_inicio']" />
      <GenericItem :item="items['fecha_fin']" />
      <GenericItem :item="items['otro']" />
      <div class="row">
        <div class="col-10"></div>
        <div class="col-2">
          <button type="button" class="btn btn-primary" @click="search()">
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
  import {
    TextField,
    DateField, HttpRequest,
  } from "@/globaltechia/utils.ts";
  import SystemView from "@/globaltechia/views/SystemView.vue";

  const messages = ref([]);

  const items = {
    fecha_inicio: new DateField({
      name  : 'fecha_inicio'
    }),
    fecha_fin: new DateField({
      name  : 'fecha_fin'
    }),
    otro: new TextField({
      name  : 'nombre',
      label : 'Nombre Completo'
    })
  };

  const search = () => {
    messages.value = [{type:'success',msg:'Reporte generado con éxito'}];

    let req = HttpRequest('POST','app/view');
    req.then((data) => {
     console.log(data);
    });
  };

</script>

<style scoped>

</style>
