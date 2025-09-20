<template>
  <select ref="select" class="form-select" v-model="selected" @change="handleChange">
    <option value="--">--</option>
    <option
        :value="item[props.model_key]"
        v-for="item in options"
    >{{ item[props.label] }}</option>
  </select>
</template>

<script setup>
import {nextTick, onMounted, ref, watch} from "vue";
import {getModelData, HttpRequest} from "@/globaltechia/utils.js";

  const props = defineProps(['modelValue','app','model','model_key','label']);

  const selected = ref(null);
  const options  = ref([]);
  const select   = ref(null);

  const emit = defineEmits(["update:modelValue","change"])

  onMounted(() => {
    loadData();
  });

  watch(
    () => props.modelValue,
      (newVal, oldVal) => {
        selected.value = newVal;

        if (newVal == null) {
          nextTick(() => {
            select.value.focus();
          });

        }

      }
  );

  function handleChange(event) {
    const value = event.target.value
    emit("update:modelValue", value);
    emit("change", value);
  }

  const loadData = () => {

    let params = {
      app       : props.app,
      model     : props.model,
      model_key : props.model_key,
      label     : props.label
    };

    getModelData(props.app,props.model,[props.model_key,props.label]).then((ev) => ev.json()).then((data) => {
      options.value = data.data;
    });
}

</script>

<style scoped>

</style>
