<template>
  <GenericView>
    <template #header>
      <ListButton to="list_user" :app="$route.params.app" view="User" />
    </template>
    <template #body>
      <h1 class="text-center">Usuario</h1>
      <h2 class="text-center"></h2>
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
                  <div class="col-6">
                    <GenericItem :item="items.first_name" />
                    <GenericItem :item="items.last_name" />
                    <GenericItem :item="items.middle_name" />
                    <GenericItem :item="items.email" />
                  </div>
                  <div class="col-6">
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
                  <div class="col-2">
                    <button class="btn btn-sm btn-primary" @click="addGroup" v-if="$route.params.id">
                      <span class="fa fa-plus-circle"></span>
                      Agregar
                    </button>
                  </div>
                </div>
                <p></p>
                <table class="table table-bordered table-condensed table-sm">
                  <thead>
                    <tr>
                      <th>Grupo</th>
                      <th>Acciones</th>
                    </tr>
                  </thead>
                </table>
              </div>
              <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">
                <div class="row">
                  <div class="col-2">
                    <button class="btn btn-sm btn-primary" @click="addPermission" v-if="$route.params.id">
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
                      <th>Acciones</th>
                    </tr>
                  </thead>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
      <component :is="last_component"></component>
    </template>
  </GenericView>

</template>

<script setup>
import {onMounted, ref} from "vue";
import { useRoute } from 'vue-router'
import {CharField, BooleanField, openModal, PasswordField, getForm} from "@/globaltechia/utils.js";
import PruebaModal from "@/modals/PruebaModal.vue";
import PruebaModalSegundo from "@/modals/PruebaModalSegundo.vue";
import GenericItem from "@/globaltechia/components/GenericItem.vue";
import GenericView from "@/globaltechia/components/GenericView.vue";
import ListButton from "@/globaltechia/components/buttons/ListButton.vue";
const items = ref({});
const last_component = ref(null);

const route = useRoute()

onMounted(async () => {
  items.value = await getForm("base","User", route.params.id);
  items.value['password']         = new PasswordField({required:false,name:"password",label_class:"col-4",input_class:'col-6'});
  items.value['confirm_password'] = new PasswordField({required:false,name:"confirm_password",label_class:"col-4",input_class:'col-6'});
});
const onChange = (value) => {
  if (items?.value.password.value !== items?.value.confirm_password.value) {
    items.value.confirm_password.error = "Verifique las contraseñas, deben de ser iguales.";
  }
  else {
    items.value.confirm_password.error = null;
  }

}
const addGroup = () => {
  openModal(last_component,PruebaModal);
}

const addPermission = () => {
  openModal(last_component,PruebaModalSegundo);
}

</script>

<style scoped>

</style>