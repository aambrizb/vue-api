<template>
  <GenericModalView>
    <template #modal_title>
      Holis
    </template>
    <template #modal_body>
      juajuajuajua que onda con esto
      {{ props.pk }} {{ props.name }}
    </template>
  </GenericModalView>
</template>

<script setup>
import GenericModalView from "@/globaltechia/components/GenericModalView.vue";
const props = defineProps(['pk','name']);
</script>

<style scoped>

</style>
