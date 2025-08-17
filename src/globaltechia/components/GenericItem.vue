<template>
  <div class="row m-1">
    <div :class="item.label_class">
      <span v-if="item.required" class="text-danger">*</span>
      {{ item.label }}
    </div>
    <div :class="item.input_class">
      <div class="row" v-if="item.type == 'text' || item.type == 'password' || item.type == 'date' || item.type == 'datetime-local' || item.type == 'checkbox'">
        <input :type="item.type" :class="getInputClass(item)" v-model="item.value" :disabled="item.disabled"/>
      </div>
      <div class="row" v-if="item.type == 'select'">
        <select :class="getInputClass(item)" v-model="item.value" :disabled="item.disabled">
          <option v-for="x in item.choices" :value="x.value">{{ x.label }}</option>
        </select>
      </div>
      <div class="row" v-if="item.type == 'textarea'">
        <textarea :class="getInputClass(item)" v-model="item.value" :disabled="item.disabled"></textarea>
      </div>
      <div class="row text-muted" v-if="item.help_text" style="font-size:11px;">
        <div class="col-12">
          {{ item.help_text }}
        </div>
      </div>
      <div class="row text-danger" v-if="item.error">
        <div class="col-12">
          <span class="fa fa-exclamation-circle"></span>
          {{ item.error }}
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>

  const props = defineProps(['item'])
  const getInputClass = ((item) => {
    let _tmp_class = item?.klass;

    if (item?.error) {
      _tmp_class += " border-danger";
    }

    return _tmp_class;
  });

</script>

<style scoped>

</style>
