field = (
  item_class:string,
  name:string,
  label:string,
  help_text:string,
  required:boolean,
  error:string,



) => {
  return {
     type        : 'input',
     name        : 'fecha_inicio',
     label       : 'Fecha de Inicio',
     help_text   : null,
     required    : true,
     error       : null,
     value       : null,
     disabled    : false,
     klass       : 'form-control',
     label_class : 'col-lg-2 col-md-2 col-sm-2 col-xs-12',
     input_class : 'col-lg-2 col-md-2 col-sm-2 col-xs-12'
   };
}


class FormField {
   constructor(type, name, label, help_text, required, error, value, disabled, klass,label_class,input_class) {
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

   }
}

field = FormField()
