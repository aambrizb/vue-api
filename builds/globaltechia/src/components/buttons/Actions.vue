<template>
  <div class="row">
    <div class="col-lg-2 col-md-2 col-xs-12">
      <button class="btn btn-sm btn-danger" @click="handlerDelete" v-if="show_delete">
        <span class="fa fa-trash"></span>
        Eliminar
      </button>
    </div>
    <div class="col-4"></div>
    <div class="col-lg-6 col-md-6 col-xs-12 text-right">
      <button class="btn btn-sm btn-outline-secondary m-1" @click="handlerSave">
        <span class="fa fa-save"></span>
        Guardar y crear otro
      </button>
      <button class="btn btn-sm btn-outline-secondary m-1" @click="handlerSave">
        <span class="fa fa-save"></span>
        Guardar y continuar editando
      </button>

      <button class="btn btn-sm btn-primary m-1" @click="handlerSave">
        <span class="fa fa-save"></span>
        Guardar
      </button>
    </div>
  </div>
</template>

<script setup>
  const props = defineProps(['show_delete']);
  const emit  = defineEmits(["delete","save"]);

  const handlerDelete = (ev) => {
    emit("delete",ev);
  }

  const handlerSave = (ev) => {
    emit("save",ev);
  }
</script>

<style scoped>

</style>
