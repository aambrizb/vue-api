<template>
  <a class="btn btn-sm btn-primary pull-right" :href="'/view/'+props.app+'/'+props.view">
    <span class="fa fa-folder" ></span>
    Nuevo
  </a>
</template>

<script setup>
  const props = defineProps(['to','app','view']);
</script>

<style scoped>

</style>