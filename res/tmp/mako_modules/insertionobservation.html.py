# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686085706.1513257
_enable_loop = True
_template_filename = 'res/templates/insertionobservation.html'
_template_uri = 'insertionobservation.html'
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
        mesObjet = context.get('mesObjet', UNDEFINED)
        mesMateriel = context.get('mesMateriel', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h3>Insertion d\'un observation</h3>\r\n\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n <form action="insertionobservationDone" method="POST" class="needs-validation insertForm" novalidate>\r\n  \r\n  <div class="form-group">\r\n    <label class="form">\r\n    <label for="date"><span class="star">*</span>Date de l\'observation :</label>\r\n    <input type="date" class="form-control" id="date" placeholder="Date de l\'observation" name="date" required>\r\n    </label>\r\n  </div>\r\n\r\n  <div class="form-group">\r\n    <label for="lieu" class="modern-label"><span class="star">*</span>Lieu:</label>\r\n    <input type="text" class="modern-input" id="lieu" placeholder="Entrer le lieu" name="lieu" required>\r\n    <div class="valid-feedback">Valide.</div>\r\n    <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n  </div>\r\n  \r\n  <div class="form-group">\r\n    <label for="observatoire" class="modern-label">Observatoire:</label>\r\n    <input type="text" class="modern-input" id="observatoire" placeholder="Entrer un observatoire" name="observatoire">\r\n    <div class="valid-feedback">Valide.</div>\r\n    <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n  </div>\r\n\r\n  <div class="form-group">\r\n    <label for="filmObjet" class="modern-label">Film:</label>\r\n    <input type="text" class="modern-input" id="filmObjet" placeholder="Entrer un film" name="filmObjet">\r\n    <div class="valid-feedback">Valide.</div>\r\n    <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n  </div>\r\n\r\n  <div class="form-group">\r\n    <label for="type" class="modern-label"><span class="star">*</span>Type :</label>\r\n    <select class="modern-select" id="type" name="type" required>\r\n      <option value="" selected disabled>Sélectionnez le type</option>\r\n      <option value="soirée">soirée</option>\r\n      <option value="journée">journée</option>\r\n    </select>\r\n    <div class="valid-feedback">Valide.</div>\r\n    <div class="invalid-feedback">Veuillez remplir ce champ, s\'il vous plaît !</div>\r\n  </div>\r\n\r\n  <div class="form-group">\r\n    <label for="materiel" class="modern-label">Matériel:</label>\r\n        <select class="modern-select" name="materiel" id="materiel">\r\n          <!-- Boucle pour afficher les options -->\r\n')
        for e in mesMateriel:
            __M_writer('          <option value="')
            __M_writer(str(e))
            __M_writer('">')
            __M_writer(str(e))
            __M_writer('</option>\r\n')
        __M_writer('        </select>\r\n  </div>\r\n\r\n  <div class="form-group">\r\n    <label for="objetObserve" class="modern-label">Objet observé:</label>\r\n        <select class="modern-select" name="objetObserve" id="objetObserve">\r\n          <!-- Boucle pour afficher les options -->\r\n')
        for e in mesObjet:
            __M_writer('          <option value="')
            __M_writer(str(e))
            __M_writer('">')
            __M_writer(str(e))
            __M_writer('</option>\r\n')
        __M_writer('        </select>\r\n  </div>\r\n\r\n  <button type="submit" class="btn btn-primary modern-button">Insérer</button>\r\n</form>\r\n\r\n<script>\r\n// Disable form submissions if there are invalid fields\r\n(function() {\r\n  \'use strict\';\r\n  window.addEventListener(\'load\', function() {\r\n    // Get the forms we want to add validation styles to\r\n    var forms = document.getElementsByClassName(\'needs-validation\');\r\n    // Loop over them and prevent submission\r\n    var validation = Array.prototype.filter.call(forms, function(form) {\r\n      form.addEventListener(\'submit\', function(event) {\r\n        if (form.checkValidity() === false) {\r\n          event.preventDefault();\r\n          event.stopPropagation();\r\n        }\r\n        form.classList.add(\'was-validated\');\r\n      }, false);\r\n    });\r\n  }, false);\r\n})();\r\n</script> ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/insertionobservation.html", "uri": "insertionobservation.html", "source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "37": 5, "38": 5, "39": 5, "40": 5, "41": 52, "42": 53, "43": 53, "44": 53, "45": 53, "46": 53, "47": 55, "48": 62, "49": 63, "50": 63, "51": 63, "52": 63, "53": 63, "54": 65, "60": 54}}
__M_END_METADATA
"""
