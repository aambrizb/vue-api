<template>
  <slot name="theme" />

  <component :is="last_component" v-bind="last_component_params"></component>

</template>

<script setup>
  import './assets/css/sb-admin-2.min.css';
  import {last_component, last_component_params} from "../../utils";
</script>

<style scoped>

</style>
