<template>
  <div class="modal fade" id="frame_modal" tabindex="-1" aria-labelledby="frame_modal" aria-hidden="true">
    <div class="modal-dialog" :class="custom_class">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="frame_modalLabel">
            <slot name="modal_title"></slot>
          </h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <slot name="modal_body"></slot>
        </div>
        <div class="modal-footer">
          <slot name="modal_footer"></slot>
        </div>
      </div>
  </div>
</div>
</template>

<script setup>
  const props = defineProps(['custom_class']);
</script>

<style scoped>

</style>
