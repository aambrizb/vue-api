<template>
  <div class="p-1">
    <input type="hidden" ref="select" v-model="selected" @change="handleChange" />
    <div class="input-group">
      <input ref="input_select" type="text" v-model="selectedValue" class="form-control" @focus="handleFocus(true);" @focusout="handleFocus(false)" @keydown="handleDown" @keyup="handleUp"/>
      <button type="button" class="btn btn-sm btn-secondary" @click="input_select.focus();">
        <span class="fa fa-angle-down" />
      </button>
    </div>
    <span v-if="loading">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </span>
    <ul id="list_select" v-if="searching">
      <li ref="listItems" v-for="item in data" :class="item === last_hover ? 'selected':''" @mouseover="overOption(item)" @click="selectedItem(item);">
        {{ item[props.label]}}
      </li>
    </ul>
  </div>

</template>

<script setup>
import {nextTick, onMounted, ref, watch} from "vue";
import {getModelData} from "../utils";


  const props = defineProps(['modelValue','app','model','model_key','label']);

  const listItems = ref([])
  const input_select  = ref(null);
  const selected_id   = ref(null);
  const selected      = ref(null);
  const selectedValue = ref(null);
  const data          = ref([]);
  const select        = ref(null);
  const searching     = ref(false);
  const last_hover    = ref(null);
  const loading       = ref(false);

  const emit = defineEmits(["update:modelValue","change"])

  onMounted(() => {
    loadData();
  });

  watch(
    () => props.modelValue,
      (newVal, oldVal) => {
        selectById(newVal);
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

  const selectById = (id) => {
    selected_id.value = id;
  }

  const selectedById = (id) => {
    let index = data.value.findIndex((item) => item[props.model_key] === id);
    selectedItem(data.value[index]);
  }

  const loadData = (text=null) => {

    let _filters = {}

    if (text) {
      _filters[props.label+"__icontains"] = text;
    }

    loading.value = true;

    getModelData(props.app,props.model,[props.model_key,props.label],_filters).then((ev) => ev.json()).then((json_data) => {

      loading.value = false;

      data.value = json_data.data;
      if (selected_id.value) {
        selectedById(selected_id.value);
      }

    });
  }

  const handleFocus = (value) => {
    setTimeout(function() {
      searching.value = value;
    },180);

  }

  const overOption = (item) => {
    last_hover.value = item;
  }

  const selectedItem = (item) => {

    if (item && item !== undefined) {
      selected.value = item;
      selectedValue.value = item[props.label];
      searching.value = false;

      emit("update:modelValue", item[props.model_key]);
      emit("change", item[props.model_key]);
    }

  }

  const handleDown = (ev) => {

    if (!searching.value) {
      return false;
    }

    if (ev.keyCode === 13) {
      if (last_hover.value) {
        selectedItem(last_hover.value);
      }
    }
    else if (ev.keyCode === 40) {
      if (!last_hover.value && data.value.length > 0) {
        last_hover.value = data.value[0];
      }
      else {
        let index = data.value.findIndex((item) => item === last_hover.value);
        if (index < data.value.length+1) {
          index += 1
        }

        last_hover.value = data.value[index];

        const el = listItems.value[index]
        if (el) {
          el.scrollIntoView({behavior:"smooth",block:"nearest"})
        }

      }
    }
    else if (ev.keyCode === 38) {
      if (!last_hover.value && data.value.length > 0) {
        last_hover.value = data.value[0];
      }
      else {
        let index = data.value.findIndex((item) => item === last_hover.value);
        if (index !== 0) {
          index -= 1;
        }

        last_hover.value = data.value[index];

        const el = listItems.value[index]
        if (el) {
          el.scrollIntoView({behavior:"smooth",block:"nearest"})
        }

      }
    }

  }

  const handleUp = (ev) => {
    if (ev.keyCode !== 13 && ev.keyCode !== 40 && ev.keyCode !== 38) {
      selected_id.value = null;
      loadData(selectedValue.value);
    }

  }

</script>

<style scoped>
  #list_select {
      list-style: none;
      padding:10px;
      margin:0px;
      max-height: 250px;
      width:100%;
      overflow:auto;
      position:absolute;
      z-index:9999;
      background-color:white;
      border-radius:15px;
      box-shadow:
        2px 2px gray,
        -.5em 0 0.8em lightgray;
  }

  #list_select li {
      cursor:pointer;
      font-size:13px;
  }

  #list_select li:hover {
      font-weight: bold;
  }

  .selected {
      font-weight: bold;
      background-color:lightgray;
      border-radius:10px;
      padding:2px;
  }
</style>
