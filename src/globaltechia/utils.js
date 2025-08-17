import {createRouter, createWebHistory} from "vue-router";
import LoginView from "@/globaltechia/views/LoginView.vue";
import SystemView from "@/globaltechia/views/SystemView.vue";
import GenericModelView from "@/globaltechia/components/GenericModelView.vue";
import GenericList from "@/globaltechia/components/GenericList.vue";

function toCapital(item) {
  let words = item.replace("_"," ");
  let final_words = "";

  let split_words = words.split(" ");
  split_words.forEach((x) => {
    final_words += x.charAt(0).toUpperCase() + x.slice(1)+ " ";
  });

  return final_words;
}
class FormField {
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

function isAuthenticated() {
  return !!localStorage.getItem('token')
}

function getRouter(local_routes) {

  let view_routes = [
    {
      path: ':app/:view',
      name: 'create',
      component: GenericModelView,
    },
    {
      path: ':app/:view/:id',
      name: 'edit',
      component: GenericModelView,
    },
    {
      path: ':app/:view/list',
      name: 'list',
      component: GenericList,
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
      component: LoginView,
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

async function HttpRequest(method,uri,payload) {
  const url = window['END_POINT']+"/"+uri
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

export {
   toCapital,
   FormField,
   TextField,
   TextAreaField,
   DateField,
   DateTimeField,
   SelectField,
   getRouter,
   HttpRequest
}
