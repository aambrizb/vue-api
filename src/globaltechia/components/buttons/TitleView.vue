<template>
  <h2 class="text-center">
    {{ toCapital(props.view) }}
  </h2>
  <h5 class="text-center text-secondary" v-if="props.id">
    {{ props.id }}
  </h5>
</template>

<script setup>
  import {toCapital} from "../../utils.js";

  const props = defineProps(['view','id']);
</script>

<style scoped>

</style>