<template>
  <div class="card border-light-subtle">
    <div class="card-header text-white" :class="'bg-'+props.type ">
      <span class="fa fa-exclamation-circle" v-if="props.type == 'success'"></span>
      <span class="fa fa-exclamation-triangle" v-if="props.type == 'danger'"></span>
      <span class="fa fa-exclamation" v-if="props.type == 'info'"></span>
    </div>
    <div class="card-body bg-light">
      {{ props.msg }}
    </div>
  </div>
  <p></p>
</template>

<script setup>

const props = defineProps(['type','msg']);

</script>

<style scoped>

</style>
