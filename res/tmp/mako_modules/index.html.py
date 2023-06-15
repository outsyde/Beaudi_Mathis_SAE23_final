# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686091873.5590954
_enable_loop = True
_template_filename = 'res/templates/index.html'
_template_uri = 'index.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n<pre class="bg-info text-white">\r\n\r\n<b>Utilisation :</b>\r\n- Tester sur Linux -> Fonctionne pas. Fonctionne sur Windows.\r\n- Pour la suppression d\'observation c\'est par le lieu de l\'observation et son numéro\r\n- Pas de présence de la partie publique, impossible à faire fonctionner..\r\n- Présence de contrainte, pour pouvoir supprimer sans soucis, il faut d\'abord supprimer une entrée dans "Observation" qui est lié au table "Matériel" et "Objet"\r\n- Par exemple : Dans table Observation -> matériel : TÉLÉSCOPE DE CATADIOPTRIQUE et objet observé : Vénus\r\n=> Il faudra d\'abord supprimer cette entrée de la table "Observation" pour supprimer dans Matériel "TÉLÉSCOPE DE CATADIOPTRIQUE" et dans Objets célestes "Vénus"\r\n\r\n<form action="loadCSVMateriel">\r\n    <button type="submit" class="btn btn-primary modern-button">Charger le CSV de Materiel</button>\r\n</form>\r\n<form action="loadCSVObjet">\r\n    <button type="submit" class="btn btn-primary modern-button">Charger le CSV d\'Objet</button>\r\n</form>\r\n<form action="loadCSVObservation">\r\n    <button type="submit" class="btn btn-primary modern-button">Charger le CSV d\'Observation</button>\r\n</form>\r\n\r\n</pre>\r\n\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 2, "34": 26, "40": 34}}
__M_END_METADATA
"""
