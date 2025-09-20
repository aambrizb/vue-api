<template>
  <div class="container-fluid p-2">
    <div class="card">
      <div class="card-header">
        <div class="row">
          <div class="col-lg-11 col-md-10 col-sm-11 col-xs-12">
            <slot name="header" />
          </div>
          <div class="col-lg-1 col-md-2 col-sm-1 col-xs-12 align-middle">
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
import Notification from "./Notification.vue";

const props = defineProps(['messages']);

</script>

<style scoped>

</style>
