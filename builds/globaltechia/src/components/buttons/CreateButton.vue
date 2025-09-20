<template>
  <router-link class="btn btn-sm btn-primary pull-right" :to="{ name: props.to, params: { 'app':props.app,'view': props.view }}">
    <span class="fa fa-folder"></span>
    Nuevo
  </router-link>
</template>

<script setup>
  const props = defineProps(['to','app','view']);
</script>

<style scoped>

</style>