<template>
  <GenericView>
    <template #header>
      <TitleView :view="name" :id="$route.params.id" />
    </template>
    <template #top_button>
      <ListButton to="list_group" :app="$route.params.app" view="Group" />
    </template>
    <template #body>
      <div class="container-fluid">
        <div class="card">
          <div class="card-body">
            <ul class="nav nav-tabs" id="myTab" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">
                  <span class="fa fa-cog"></span>
                  General
                </button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="contact-tab" data-bs-toggle="tab" data-bs-target="#contact" type="button" role="tab" aria-controls="contact" aria-selected="false">
                  <span class="fa fa-list"></span>
                  Permisos
                </button>
              </li>
            </ul>
            <div class="tab-content p-4" id="myTabContent">
              <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                <GenericForm :items="items" />
              </div>
              <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">
                <div class="row">
                  <div class="col-lg-2 col-md-2 col-xs-12">Permiso</div>
                  <div class="col-lg-3 col-md-3 col-xs-12">
                    <SelectModel v-model="selected_permission" app="base" model="Permission" model_key="id" label="name" />
                  </div>
                  <div class="col-lg-3 col-md-3 col-xs-12">
                    <button type="button" class="btn btn-primary btn-sm" @click="addPermission">
                      <span class="fa fa-plus-circle"></span>
                      Agregar
                    </button>
                  </div>
                </div>
                <p></p>
                <table class="table table-bordered table-condensed table-sm">
                  <thead>
                    <tr>
                      <th>Permiso</th>
                      <th class="text-center">Acciones</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in data_grouppermission">
                      <td class="col-10">{{ item.permission__name }}</td>
                      <td class="col-2 text-center">
                        <span class="fa fa-trash-can text-danger" style="cursor:pointer;" @click="removePermission(item)"/>
                      </td>
                    </tr>
                  </tbody>

                </table>
              </div>
            </div>
          </div>
        </div>
      </div>

    </template>
    <template #footer>
      <Actions @save="btnSave" @delete="btnDelete" :show_delete="$route.params.id ? true:false" />
    </template>
  </GenericView>

</template>

<script setup>
import {onMounted, ref} from "vue";
import { useRoute, useRouter } from 'vue-router'
import {
  getForm,
  removeModel,
  addModel,
  getModelData,
  DefaultBtnSave,
  DefaultBtnDelete,
  ValidateData,
  getFormData
} from "../utils";
import GenericView from "../components/GenericView.vue";
import ListButton from "../components/buttons/ListButton.vue";
import TitleView from "../components/buttons/TitleView.vue";
import SelectModel from "../components/SelectModel.vue";
import Actions from "../components/buttons/Actions.vue";
import Swal from "sweetalert2";
import GenericForm from "../components/GenericForm.vue";

const module_name = ref("Group");
const name        = ref("");
const items       = ref({});

const router = useRouter();
const route  = useRoute();

const selected_permission = ref(null);

const data_grouppermission = ref([]);

onMounted(async () => {

  await getForm("base","Group", route.params.id).then((data) => {
    name.value = data.verbose_name;
    items.value = data.form;
  });

  loadGroupPermissions();

});

const loadGroupPermissions = () => {
  getModelData("base","GroupPermission",["id","permission__name"],{"group_id":route.params.id}).then((ev) => ev.json()).then((data) => {
    data_grouppermission.value = data.data;
  });
}

const addPermission = () => {
  Swal.fire({
    title: "¿Realmente desea agregar este elemento?",
    showDenyButton: true,
    confirmButtonText: "Si",
    denyButtonText: `No`
  }).then((result) => {
    if (result.isConfirmed) {
      let params = {
        "group_id"      : route.params.id,
        "permission_id" : selected_permission.value,
      }

      addModel("base","GroupPermission",params).then((ev) => ev.json()).then((data) => {
        if (data.code === 200) {
          selected_permission.value = null;
          loadGroupPermissions();
        }
      });
    }
  });

}

const removePermission = (item) => {
    Swal.fire({
    title: "¿Realmente desea eliminar este elemento?",
    showDenyButton: true,
    confirmButtonText: "Si",
    denyButtonText: `No`
  }).then((result) => {
    if (result.isConfirmed) {
      removeModel("base","GroupPermission",item.id).then((ev) => ev.json()).then((data) => {
        if (data.code === 200) {
          loadGroupPermissions();
        }
      });
    }
  });

}

const btnSave = (ev,extra) => {

  let is_valid = ValidateData(items.value);
  let data     = getFormData(items.value);

  if (!is_valid) return;

  DefaultBtnSave(extra,route.params.app,module_name.value,data,route.params.id);

}

const btnDelete = () => {
  DefaultBtnDelete(route.params.app,module_name.value,route.params.id);
}

</script>

<style scoped>

</style>
