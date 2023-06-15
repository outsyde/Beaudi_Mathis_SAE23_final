# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686074968.0355365
_enable_loop = True
_template_filename = 'res/templates/supprimermateriel.html'
_template_uri = 'supprimermateriel.html'
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
        message = context.get('message', UNDEFINED)
        mesMaterielsId = context.get('mesMaterielsId', UNDEFINED)
        type = context.get('type', UNDEFINED)
        mesMateriels = context.get('mesMateriels', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n<h3 class="suppressionmateriel">Suppression de materiel par son numéro</h3>\r\n\r\n<div class="containerSuppr">\r\n  <p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('" id="messagebanner">')
        __M_writer(str(message))
        __M_writer('</p>\r\n')
        for e in mesMateriels:
            __M_writer('  <div class="materiel">\r\n      ')
            __M_writer(str(e))
            __M_writer(' <br />\r\n  </div>\r\n')
        __M_writer('</div>\r\n\r\n<form action="supprimermateriel" method="POST" class="modern-form">\r\n  <div class="form-group">\r\n    <label for="numMateriel" class="modern-label">Numéro:</label>\r\n        <select class="modern-select" name="numMateriel" id="numMateriel">\r\n          <!-- Boucle pour afficher les options -->\r\n')
        for e in mesMaterielsId:
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
{"filename": "res/templates/supprimermateriel.html", "uri": "supprimermateriel.html", "source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "37": 2, "38": 7, "39": 7, "40": 7, "41": 7, "42": 8, "43": 9, "44": 10, "45": 10, "46": 13, "47": 20, "48": 21, "49": 21, "50": 21, "51": 21, "52": 21, "53": 23, "54": 30, "60": 54}}
__M_END_METADATA
"""
