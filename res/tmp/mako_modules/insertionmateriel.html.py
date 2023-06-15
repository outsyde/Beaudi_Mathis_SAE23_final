# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686086011.244558
_enable_loop = True
_template_filename = 'res/templates/insertionmateriel.html'
_template_uri = 'insertionmateriel.html'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'template.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        type = context.get('type', UNDEFINED)
        message = context.get('message', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h3>Insertion d\'un objet céleste</h3>\r\n\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n <form action="insertionmaterielDone" method="POST" class="needs-validation insertForm" novalidate>\r\n  \r\n  <div class="form-group">\r\n    <label for="type" class="modern-label"><span class="star">*</span>Type :</label>\r\n    <select class="modern-select" id="type" name="type" required>\r\n      <option value="" selected disabled>Sélectionnez le type</option>\r\n      <option value="TÉLÉSCOPE DE NEWTON">TÉLÉSCOPE DE NEWTON</option>\r\n      <option value="TÉLÉSCOPE DE CASSEGRAIN">TÉLÉSCOPE DE CASSEGRAIN</option>\r\n      <option value="TÉLÉSCOPE CATADIOPTRIQUE">TÉLÉSCOPE CATADIOPTRIQUE</option>\r\n    </select>\r\n    <div class="valid-feedback">Valide.</div>\r\n    <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n  </div>\r\n\r\n  <div class="form-group">\r\n    <label for="prix" class="modern-label"><span class="star">*</span>Prix:</label>\r\n    <input type="number" class="modern-input" id="prix" placeholder="Entrer le prix" name="prix" step="1">\r\n    <div class="valid-feedback">Valide.</div>\r\n    <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n  </div>\r\n\r\n  <button type="submit" class="btn btn-primary modern-button">Insérer</button>\r\n</form>\r\n\r\n<script>\r\n// Disable form submissions if there are invalid fields\r\n(function() {\r\n  \'use strict\';\r\n  window.addEventListener(\'load\', function() {\r\n    // Get the forms we want to add validation styles to\r\n    var forms = document.getElementsByClassName(\'needs-validation\');\r\n    // Loop over them and prevent submission\r\n    var validation = Array.prototype.filter.call(forms, function(form) {\r\n      form.addEventListener(\'submit\', function(event) {\r\n        if (form.checkValidity() === false) {\r\n          event.preventDefault();\r\n          event.stopPropagation();\r\n        }\r\n        form.classList.add(\'was-validated\');\r\n      }, false);\r\n    });\r\n  }, false);\r\n})();\r\n</script> ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/insertionmateriel.html", "uri": "insertionmateriel.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 5, "36": 5, "37": 5, "38": 5, "44": 38}}
__M_END_METADATA
"""
