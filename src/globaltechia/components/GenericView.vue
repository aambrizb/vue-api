<template>
  <div class="container-fluid p-2">
    <div class="card">
      <div class="card-header">
        <div class="row">
          <div class="col-11">
            <slot name="header" />
          </div>
          <div class="col-1 align-middle">
            <slot name="top_button" />
          </div>
        </div>
      </div>
      <div class="card-body">
        <Notification v-for="msg in props.messages" :type="msg.type" :msg="msg.msg"/>
        <slot name="body" />
      </div>
      <div class="card-footer">
        <slot name="footer" />
      </div>
    </div>
  </div>

</template>

<script setup>
import Notification from "@/globaltechia/components/Notification.vue";

const props = defineProps(['messages']);

</script>

<style scoped>

</style>
