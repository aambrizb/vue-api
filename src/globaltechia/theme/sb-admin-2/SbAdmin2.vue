<template>
  <slot name="theme" />

  <component :is="last_component" v-bind="last_component_params"></component>

</template>

<script setup>
  import '@/globaltechia/theme/sb-admin-2/assets/css/sb-admin-2.min.css';
  import {last_component, last_component_params} from "@/globaltechia/utils.js";
</script>

<style scoped>

</style>
