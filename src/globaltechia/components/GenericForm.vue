<template>
  <GenericItem :item="item" v-for="item in props.items" />
</template>

<script setup>
 import GenericItem from "@/globaltechia/components/GenericItem.vue";

 const props = defineProps(['items']);

 const is_valid = () => {

   let valid = true;

   Object.keys(props.items).forEach((key) => {
     let item = props.items[key];
     if (item.required && !item.value) {
       item.error = "Es requerido capturar este campo."
       valid = false;
     }
   });

   return valid;

 };

 const data = () => {
  let final_data = {};
  Object.keys(props.items).forEach((key) => {
    let item = props.items[key];

    if (item.type !== 'checkbox') {
      final_data[item.name] = item.value;
    }
    else {
      final_data[item.name] = item.value ? item.value:false;
    }

  });

  return final_data;
 };

 defineExpose({
   is_valid,
   data
 });

</script>

<style scoped>

</style>
