<template>
  <div v-if="show" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
    <div class="bg-white rounded-lg p-6 w-96 relative">
      <button class="absolute top-2 right-2" @click="$emit('close')">❌</button>
      <component :is="component"></component>
    </div>
  </div>
</template>

<script setup>
  const props = defineProps(['show','component']);
</script>

<style scoped>

</style>
