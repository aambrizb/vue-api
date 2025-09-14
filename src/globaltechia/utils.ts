import {createRouter, createWebHistory} from "vue-router";
import LoginView from "@/globaltechia/views/LoginView.vue";
import SystemView from "@/globaltechia/views/SystemView.vue";
import GenericModelView from "@/globaltechia/components/GenericModelView.vue";
import GenericList from "@/globaltechia/components/GenericList.vue";
import DashboardView from "@/globaltechia/views/DashboardView.vue";
import UserView from "@/globaltechia/views/UserView.vue";
import { Modal } from 'bootstrap';

function toCapital(item:string|undefined|null) {

  let words       = ""
  let final_words = ""

  if (item !== undefined && item !== null) {
    words = item.replace("_"," ");
  }

  let split_words = words.split(" ");
  split_words.forEach((x) => {
    final_words += x.charAt(0).toUpperCase() + x.slice(1)+ " ";
  });

  return final_words;
}
class FormField {

    type: string | undefined | null
    name: string | undefined | null
    label: string | undefined | null
    help_text: string | undefined | null
    required: boolean
    error: string | undefined | null
    value: string | undefined | null
    disabled: boolean
    klass: string | undefined | null
    label_class: string | undefined | null
    input_class: string | undefined | null

   constructor({
                  type = null,
                  name = null,
                  label = '',
                  help_text = '',
                  required = true,
                  error = null,
                  value = null,
                  disabled = false,
                  klass = 'form-control',
                  label_class = 'col-lg-2 col-md-2 col-sm-2 col-xs-12',
                  input_class = 'col-lg-2 col-md-2 col-sm-2 col-xs-12'
               }) {
      this.type        = type;
      this.name        = name;
      this.label       = label;
      this.help_text   = help_text;
      this.required    = required;
      this.error       = error;
      this.value       = value;
      this.disabled    = disabled;
      this.klass       = klass;
      this.label_class = label_class;
      this.input_class = input_class;

      if (!this.label || this.label == '' || this.label == undefined) {
        this.label = toCapital(this.name);
      }

   }
}

class CharField extends FormField {
 type = 'text'
}

class PasswordField extends FormField {
 type = 'password'
}
class TextField extends FormField {
 type = 'text'
}

class TextAreaField extends FormField {
  type = 'textarea'
}

class DateField extends FormField {
  type = 'date'
}

class DateTimeField extends FormField {
  type = 'datetime'
}

class SelectField extends FormField {
  type = 'select'
}

class BooleanField extends FormField {
  type = 'checkbox'
  klass = ''
}

function isAuthenticated() {
  return !!localStorage.getItem('token')
}

function getRouter(local_routes:any,_loginView:any,_dashboardView:any) {

  if (_loginView === undefined) {
    _loginView = LoginView
  }

  if (_dashboardView === undefined) {
    _dashboardView = DashboardView
  }

  let view_routes = [
    {
      path      : '',
      name      : 'dashboard',
      component : _dashboardView,
    },
    {
      path      : ':app/:view',
      name      : 'create',
      component : GenericModelView,
    },
    {
      path      : ':app/:view/:id',
      name      : 'edit',
      component : GenericModelView,
    },
    {
      path      : ':app/:view/list',
      name      : 'list',
      component : GenericList,
    },
    {
      path      : ':app/User',
      name      : 'user',
      component : UserView,
    }
  ];

  let final_routes = view_routes.concat(local_routes);

  let base_route = [
    {
      path: '/',
      redirect: () => (isAuthenticated() ? '/view' : '/login')
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/'
    },
    {
      path: '/login',
      name: 'login',
      component: _loginView,
    },
    {
      path: '/view',
      component: SystemView,
      children: final_routes
    }
  ]

  let router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: base_route
  });

  router.beforeEach((to, from, next) => {
    if (to.name !== 'login' && !isAuthenticated()) {
      return next('/login')
    }

    next()

  })

  return router;

}

async function HttpRequest(method:string,uri:string,payload:any) {
  const url = window.END_POINT+"/"+uri

  let body = null;

  if (payload !== undefined) {
    body = JSON.stringify(payload)
  }

  return await fetch(url,{
    method  : method,
    headers : {
      'Content-Type':'application/json'
    },
    body    : body,
  });


}

async function getForm(app,view,id) {

  let items = {};
  let full_uri = app+"/"+view;

  if (id) {
    full_uri += "/"+id;
  }

  const response = await HttpRequest("GET",full_uri);
  const data     = await response.json()

  if (response.status == 200) {
    return data.form;
  }

}

function openModal(last_component:any,component:any) {

  last_component.value = component;

  setTimeout(function() {
    var last = document.getElementById('frame_modal');
    if (last) {
      var myModal = new Modal(last);
      myModal.show();
    }

  },200);

};

export {
   toCapital,
   FormField,
   CharField,
   PasswordField,
   TextField,
   TextAreaField,
   DateField,
   DateTimeField,
   SelectField,
   BooleanField,
   getRouter,
   HttpRequest,
   getForm,
   openModal
}
