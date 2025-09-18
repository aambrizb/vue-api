<template>
  <div class="row">
    <div class="col-2">
      <button class="btn btn-danger" @click="handlerDelete">
        <span class="fa fa-trash"></span>
        Eliminar
      </button>
    </div>
    <div class="col-8"></div>
    <div class="col-2 text-right">
      <button class="btn btn-primary" @click="handlerSave">
        <span class="fa fa-save"></span>
        Guardar
      </button>
    </div>
  </div>
</template>

<script setup>
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