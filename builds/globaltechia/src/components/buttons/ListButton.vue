<template>
  <div class="row">
    <div class="col-11"></div>
    <div class="col-1">
      <router-link class="btn btn-sm btn-secondary pull-right" :to="{ name: props.to, params: { 'app':props.app,'view': props.view }}">
        <span class="fa fa-list"></span>
        Listar
      </router-link>
    </div>
  </div>

</template>

<script setup>
  const props = defineProps(['to','app','view']);
</script>

<style scoped>

</style>