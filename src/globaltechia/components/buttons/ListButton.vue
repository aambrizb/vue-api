<template>
  <div class="row">
    <div class="col-11"></div>
    <div class="col-1">
      <a class="btn btn-sm btn-secondary pull-right" :href="'/view/'+props.app+'/'+props.view+'/list'">
        <span class="fa fa-list"></span>
        Listar
      </a>
    </div>
  </div>

</template>

<script setup>
  const props = defineProps(['to','app','view']);
</script>

<style scoped>

</style>