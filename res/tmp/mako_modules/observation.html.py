# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686068996.6567538
_enable_loop = True
_template_filename = 'res/templates/observation.html'
_template_uri = 'observation.html'
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
        mesObserv = context.get('mesObserv', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n<h3 class="affichageobserv">Affichage</h3>\r\n<h3 class="listeobserv">Liste des observations</h3>\r\n\r\n<div class="container">\r\n')
        for e in mesObserv:
            __M_writer('\t<div class="observ">\r\n\t\t')
            __M_writer(str(e))
            __M_writer(' <br />\r\n\t</div>\r\n')
        __M_writer('  </div>\r\n\r\n')
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/observation.html", "uri": "observation.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 2, "35": 8, "36": 9, "37": 10, "38": 10, "39": 13, "40": 15, "46": 40}}
__M_END_METADATA
"""
