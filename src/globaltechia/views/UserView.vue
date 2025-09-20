<template>
  <GenericView>
    <template #header>
      <TitleView :view="name" :id="$route.params.id" />
    </template>
    <template #top_button>
      <ListButton to="list_user" :app="$route.params.app" view="User" />
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
                <button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">
                  <span class="fa fa-user-group"></span>
                  Grupos
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
                <div class="row">
                  <div class="col-lg-6 col-md-6 col-xs-12">
                    <GenericItem :item="items.first_name" />
                    <GenericItem :item="items.last_name" />
                    <GenericItem :item="items.middle_name" />
                    <GenericItem :item="items.email" />
                  </div>
                  <div class="col-lg-6 col-md-6 col-xs-12">
                    <GenericItem :item="items.password" @change="onChange" />
                    <GenericItem :item="items.confirm_password" @change="onChange" />
                    <div v-if="items?.password?.value !== null && (items?.password?.value == items?.confirm_password?.value)" class="text-success text-center">
                      <span class="fa fa-check-circle"></span>
                      Contraseña válida.
                    </div>
                    <GenericItem :item="items.superuser" />
                    <GenericItem :item="items.active" />
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                <div class="row">
                  <div class="col-lg-2 col-md-2 col-xs-12">Grupo</div>
                  <div class="col-lg-3 col-md-3 col-xs-12">
                    <SelectModel v-model="selected_group" app="base" model="Group" model_key="id" label="name" />
                  </div>
                  <div class="col-lg-3 col-md-3 col-xs-12">
                    <button type="button" class="btn btn-primary btn-sm" @click="addGroup">
                      <span class="fa fa-plus-circle"></span>
                      Agregar
                    </button>
                  </div>
                </div>
                <p></p>
                <table class="table table-bordered table-condensed table-sm">
                  <thead>
                    <tr>
                      <th class="col-10">Grupo</th>
                      <th class="col-2 text-center">Acciones</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in data_usergroup">
                      <td class="col-10">{{ item.group__name }}</td>
                      <td class="col-2 text-center">
                        <span class="fa fa-trash-can text-danger" style="cursor:pointer;" @click="removeGroup(item)"/>
                      </td>
                    </tr>
                  </tbody>
                </table>
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
                    <tr v-for="item in data_userpermission">
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
import { useRoute } from 'vue-router'
import {
  PasswordField,
  getForm,
  HttpRequest,
  removeModel,
  addModel,
  getModelData,
  openModal, getFullURI, getFormData, ValidateData
} from "@/globaltechia/utils.js";
import GenericItem from "@/globaltechia/components/GenericItem.vue";
import GenericView from "@/globaltechia/components/GenericView.vue";
import ListButton from "@/globaltechia/components/buttons/ListButton.vue";
import TitleView from "@/globaltechia/components/buttons/TitleView.vue";
import SelectModel from "@/globaltechia/components/SelectModel.vue";
import PruebaModal from "@/modals/PruebaModal.vue";
import router from "@/router/index.js";
import Actions from "@/globaltechia/components/buttons/Actions.vue";
import Swal from "sweetalert2";

const name  = ref("");
const items = ref({});

const route = useRoute()

const selected_group      = ref(null);
const selected_permission = ref(null);

const data_usergroup      = ref([]);
const data_userpermission = ref([]);

onMounted(async () => {

  await getForm("base","User", route.params.id).then((data) => {
    name.value = data.verbose_name;
    items.value = data.form;
  });

  items.value['password']         = new PasswordField({required:false,name:"password",label:"Contraseña",label_class:"col-lg-4 col-md-4 col-xs-12",input_class:'col-lg-6 col-md-6 col-xs-12'});
  items.value['confirm_password'] = new PasswordField({required:false,name:"confirm_password",label_class:"col-lg-4 col-md-4 col-xs-12",input_class:'col-lg-6 col-md-6 col-xs-12'});

  loadUserGroups();
  loadUserPermissions();

});

const loadUserGroups = () => {
  getModelData("base","UserGroup",["id","group__name"],{"user_id":route.params.id}).then((ev) => ev.json()).then((data) => {
    data_usergroup.value = data.data;
  });
}

const loadUserPermissions = () => {
  getModelData("base","UserPermission",["id","permission__name"],{"user_id":route.params.id}).then((ev) => ev.json()).then((data) => {
    data_userpermission.value = data.data;
  });
}

const onChange = (value) => {
  if (items?.value.password.value !== items?.value.confirm_password.value) {
    items.value.confirm_password.error = "Verifique las contraseñas, deben de ser iguales.";
  }
  else {
    items.value.confirm_password.error = null;
  }

}
const addGroup = () => {
  Swal.fire({
    title: "¿Realmente desea agregar este elemento?",
    showDenyButton: true,
    confirmButtonText: "Si",
    denyButtonText: `No`
  }).then((result) => {
    if (result.isConfirmed) {

       let params = {
        "user_id"  : route.params.id,
        "group_id" : selected_group.value,
      }

      addModel("base","UserGroup",params).then((ev) => ev.json()).then((data) => {
        if (data.code === 200) {
          selected_group.value = null;
          loadUserGroups();
        }
      });
    }
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
        "user_id"       : route.params.id,
        "permission_id" : selected_permission.value,
      }

      addModel("base","UserPermission",params).then((ev) => ev.json()).then((data) => {
        if (data.code === 200) {
          selected_permission.value = null;
          loadUserPermissions();
        }
      });
    }
  });

}
const removeGroup = (item) => {

  Swal.fire({
    title: "¿Realmente desea eliminar este elemento?",
    showDenyButton: true,
    confirmButtonText: "Si",
    denyButtonText: `No`
  }).then((result) => {
    if (result.isConfirmed) {
      removeModel("base","UserGroup",item.id).then((ev) => ev.json()).then((data) => {
        if (data.code === 200) {
          loadUserGroups();
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
      removeModel("base","UserPermission",item.id).then((ev) => ev.json()).then((data) => {
        if (data.code === 200) {
          loadUserPermissions();
        }
      });
    }
  });

}

const btnSave = () => {

  let is_valid = ValidateData(items.value);
  let data     = getFormData(items.value);
  let full_uri = getFullURI(route.params.app,"User",route.params.id);

  if (is_valid) {

    HttpRequest("POST",full_uri,data)
        .then((data_json) => data_json.json())
        .then((data) => {
          router.replace({ name: 'list_user', params: { app: route.params.app,view:route.params.view } });
        });
  }
}

const btnDelete = () => {
    Swal.fire({
      title: "¿Realmente desea eliminar este elemento?",
      showDenyButton: true,
      confirmButtonText: "Si",
      denyButtonText: `No`
    }).then((result) => {

    if (result.isConfirmed) {
      removeModel("base", "User", route.params.id).then((ev) => ev.json()).then((data) => {
        Swal.fire(data.msg, "", "success").then(() => {
          router.replace({ name: 'list_user', params: { app: route.params.app,view:route.params.view } });
        });
      });
    }
  });
}

</script>

<style scoped>

</style>
