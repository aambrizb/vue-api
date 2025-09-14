<template>
  <div class="row m-1" v-if="item">
    <div :class="item.label_class">
      <span v-if="item.required" class="text-danger">*</span>
      {{ item.label }}
    </div>
    <div :class="item.input_class">
      <div v-if="item.type == 'text' || item.type == 'password' || item.type == 'date' || item.type == 'datetime-local'">
        <input
            :type="item.type"
            :class="getInputClass(item)"
            v-model="item.value"
            :disabled="item.disabled"
            @input="$emit('update:item.value', $event.target.value)"
            @keyup="$emit('keyup', $event)"
            @change="$emit('change', $event.target.value)"
        />
      </div>
      <div v-if="item.type == 'checkbox'">
        <input
            type="checkbox"
            :class="getInputClass(item)"
            v-model="item.value"
            :disabled="item.disabled"
            :checked="item.value ? 'checked':'' "
            @input="$emit('update:item.value', $event.target.value)"
            @keyup="$emit('keyup', $event)"
            @change="$emit('change', $event.target.value)"
        />
      </div>
      <div v-if="item.type == 'select'">
        <select
            :class="getInputClass(item)"
            v-model="item.value"
            :disabled="item.disabled"
            @change="$emit('change', $event.target.value)"
        >
          <option v-for="x in item.choices" :value="x.value">{{ x.label }}</option>
        </select>
      </div>
      <div v-if="item.type == 'textarea'">
        <textarea
            :class="getInputClass(item)"
            v-model="item.value"
            :disabled="item.disabled"
            @input="$emit('update:item.value', $event.target.value)"
            @keyup="$emit('keyup', $event)"
            @change="$emit('change', $event.target.value)"
        ></textarea>
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

  defineEmits(['update:item.value', 'keyup', 'change'])

</script>

<style scoped>

</style>
