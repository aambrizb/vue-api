<template>
  <div class="row">
    <div class="col-11"></div>
    <div class="col-1">
      <button class="btn btn-sm btn-primary pull-right" @click="handlerSave">
        <span class="fa fa-save"></span>
        Guardar
      </button>
    </div>
  </div>
</template>

<script setup>

const emit  = defineEmits(["click"])

const handlerSave = (ev) => {
  emit("click",ev);
}
</script>

<style scoped>

</style>