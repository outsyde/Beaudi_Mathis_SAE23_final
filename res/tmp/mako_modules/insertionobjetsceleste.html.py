# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686085548.6506684
_enable_loop = True
_template_filename = 'res/templates/insertionobjetsceleste.html'
_template_uri = 'insertionobjetsceleste.html'
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
        __M_writer('</p>\r\n\r\n<form action="insertionobjetscelesteDone" method="POST" class="needs-validation insertForm" novalidate>\r\n  <div class="insertObjetForm">\r\n    <div class="insertObjetFormNom">\r\n      <div class="form-group">\r\n        <label for="nom"><span class="star">*</span>Nom:</label>\r\n        <input type="text" class="form-control" id="nom" placeholder="Entrer le nom de l\'astre" name="nom" required>\r\n        <div class="valid-feedback">Valide.</div>\r\n        <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît</div>\r\n      </div>\r\n\r\n      <div class="form-group">\r\n        <label for="type" class="modern-label"><span class="star">*</span>Type :</label>\r\n        <select class="modern-select" id="type" name="type" required>\r\n          <option value="" selected disabled>Sélectionnez le type</option>\r\n          <option value="Téllurique">Téllurique</option>\r\n          <option value="Gazeux">Gazeux</option>\r\n        </select>\r\n        <div class="valid-feedback">Valide.</div>\r\n        <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n      </div>\r\n    </div>\r\n\r\n  <div class="insertObjetFormOther">\r\n    <div class="form-group">\r\n      <label for="distanceTerre" class="modern-label">Distance Terre:</label>\r\n      <input type="number" class="modern-input" id="distanceTerre" placeholder="Entrer la distance à la Terre" name="distanceTerre" step="1">\r\n      <div class="valid-feedback">Valide.</div>\r\n      <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n    </div>\r\n    \r\n    <div class="form-group">\r\n      <label for="distanceSoleil" class="modern-label"><span class="star">*</span>Distance Soleil:</label>\r\n      <input type="number" class="modern-input" id="distanceSoleil" placeholder="Entrer la distance au Soleil" name="distanceSoleil" step="1" required>\r\n      <div class="valid-feedback">Valide.</div>\r\n      <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n    </div>\r\n\r\n    <div class="form-group">\r\n      <label for="distanceGalaxie" class="modern-label">Distance Galaxie:</label>\r\n      <input type="number" class="modern-input" id="distanceGalaxie" placeholder="Entrer la distance à la Galaxie" name="distanceGalaxie" step="1">\r\n      <div class="valid-feedback">Valide.</div>\r\n      <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n    </div>\r\n\r\n    <div class="form-group">\r\n      <label for="luminosite" class="modern-label">Luminosité:</label>\r\n      <input type="number" class="modern-input" id="luminosite" placeholder="Entrer la luminosite" name="luminosite" step="1">\r\n      <div class="valid-feedback">Valide.</div>\r\n      <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n    </div>\r\n\r\n    <div class="form-group">\r\n      <label for="vitesse" class="modern-label">Vitesse:</label>\r\n      <input type="number" class="modern-input" id="vitesse" placeholder="Entrer la vitesse" name="vitesse" step="1">\r\n      <div class="valid-feedback">Valide.</div>\r\n      <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n    </div>\r\n\r\n    <div class="form-group">\r\n      <label for="age" class="modern-label"><span class="star">*</span>Âge:</label>\r\n      <input type="number" class="modern-input" id="age" placeholder="Entrer l\'âge" name="age" step="1" required>\r\n      <div class="valid-feedback">Valide.</div>\r\n      <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n    </div>\r\n\r\n    <button type="submit" class="btn btn-primary modern-button">Insérer</button>\r\n  </div>\r\n\r\n  </div>\r\n</form>\r\n<script>\r\n// Disable form submissions if there are invalid fields\r\n(function() {\r\n  \'use strict\';\r\n  window.addEventListener(\'load\', function() {\r\n    // Get the forms we want to add validation styles to\r\n    var forms = document.getElementsByClassName(\'needs-validation\');\r\n    // Loop over them and prevent submission\r\n    var validation = Array.prototype.filter.call(forms, function(form) {\r\n      form.addEventListener(\'submit\', function(event) {\r\n        if (form.checkValidity() === false) {\r\n          event.preventDefault();\r\n          event.stopPropagation();\r\n        }\r\n        form.classList.add(\'was-validated\');\r\n      }, false);\r\n    });\r\n  }, false);\r\n})();\r\n</script> ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/insertionobjetsceleste.html", "uri": "insertionobjetsceleste.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 5, "36": 5, "37": 5, "38": 5, "44": 38}}
__M_END_METADATA
"""
