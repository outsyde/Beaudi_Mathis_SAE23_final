# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686071993.0094957
_enable_loop = True
_template_filename = 'res/templates/supprimerbjetsceleste.html'
_template_uri = 'supprimerbjetsceleste.html'
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
        mesObjetsId = context.get('mesObjetsId', UNDEFINED)
        message = context.get('message', UNDEFINED)
        mesObjets = context.get('mesObjets', UNDEFINED)
        type = context.get('type', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n<h3 class="suppressionobjet">Suppression d\'un objet céleste par son numéro</h3>\r\n\r\n<div class="containerSuppr">\r\n  <p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('" id="messagebanner">')
        __M_writer(str(message))
        __M_writer('</p>\r\n')
        for e in mesObjets:
            __M_writer('  <div class="objetceleste">\r\n      ')
            __M_writer(str(e))
            __M_writer(' <br />\r\n  </div>\r\n')
        __M_writer('</div>\r\n\r\n<form action="supprimerbjetsceleste" method="POST" class="modern-form">\r\n  <div class="form-group">\r\n    <label for="numObjet" class="modern-label">Numéro:</label>\r\n        <select class="modern-select" name="numObjet" id="numObjet">\r\n          <!-- Boucle pour afficher les options -->\r\n')
        for e in mesObjetsId:
            __M_writer('          <option value="')
            __M_writer(str(e))
            __M_writer('">')
            __M_writer(str(e))
            __M_writer('</option>\r\n')
        __M_writer('        </select>\r\n  </div>\r\n  <button type="submit" class="modern-button">Supprimer</button>\r\n</form>\r\n\r\n\r\n\r\n')
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/supprimerbjetsceleste.html", "uri": "supprimerbjetsceleste.html", "source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "37": 2, "38": 7, "39": 7, "40": 7, "41": 7, "42": 8, "43": 9, "44": 10, "45": 10, "46": 13, "47": 20, "48": 21, "49": 21, "50": 21, "51": 21, "52": 21, "53": 23, "54": 30, "60": 54}}
__M_END_METADATA
"""
