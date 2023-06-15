# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686086832.86874
_enable_loop = True
_template_filename = 'res/templates/template.html'
_template_uri = 'template.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!doctype html>\r\n<html lang="fr">\r\n  <head>\r\n    <meta charset="utf-8">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\r\n\r\n    <!-- Bootstrap CSS -->\r\n\t<!--\r\n    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">\r\n\t-->\r\n    <link rel="stylesheet" href="/static/css/bootstrap.min.css" >\r\n    <!-- CSS Perso -->\r\n    <link rel="stylesheet" href="/static/css/style.css" >\r\n\r\n    <title>SAE23:Astronomie</title>\r\n  </head>\r\n  <body>\r\n\r\n    <!-- Optional JavaScript -->\r\n    <!-- jQuery first, then Popper.js, then Bootstrap JS -->\r\n    <script src="/static/js/jquery-3.5.0.min.js"></script>\r\n\t<!-- Pas utile ?\r\n    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>\r\n\t-->\r\n    <script src="/static/js/bootstrap.min.js"></script>\r\n\t\r\n\t\r\n\r\n        \r\n <nav class="navbar navbar-expand-lg navbar-light bg-dark">\r\n   <div class="collapse navbar-collapse" id="navbarNavDropdown">\r\n    <ul class="navbar-nav">\r\n      <li class="nav-item active">\r\n        <a class="nav-link" href="index">Accueil</a>\r\n      </li>\r\n      <li>\r\n        <a class="nav-link" href="objetsceleste" role="button">\r\n          Objets célestes\r\n        </a>\r\n      </li>\r\n      <li class="nav-item">\r\n        <a class="nav-link" href="observation" role="button">Observation</a>\r\n      </li>\r\n      <li class="nav-item">\r\n        <a class="nav-link" href="materiel" role="button">Matériel</a>\r\n      </li>\r\n      <li class="nav-item dropdown">\r\n        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n          Suppressions\r\n        </a>\r\n        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">\r\n          <a class="dropdown-item" href="supprimerobjetsceleste">Supprimer d\'objet céleste</a>\r\n          <a class="dropdown-item" href="supprimerobservation">Supprimer d\'observation</a>\r\n          <a class="dropdown-item" href="supprimermateriel">Supprimer matériel</a>\r\n        </div>\r\n      <li class="nav-item dropdown">\r\n        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n          Insertions\r\n        </a>\r\n        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">\r\n          <a class="dropdown-item" href="insertionobjetsceleste">Insertion d\'objet céleste</a>\r\n          <a class="dropdown-item" href="insertionobservation">Insertion d\'observation</a>\r\n          <a class="dropdown-item" href="insertionmateriel">Insertion de materiel</a>\r\n        </div>\r\n      </li>\r\n    </ul>\r\n  </div>\r\n</nav>\r\n\r\n<div class="container-fluid">\r\n  <!-- Hero -->\r\n  <div class="p-5 text-center bg-image rounded-3">\r\n    <div class="mask" style="background-color: rgba(0, 0, 0, 0);">\r\n      <div class="d-flex justify-content-center align-items-center h-100">\r\n        <div class="text-white">\r\n          <h1 class="mb-3">Astronomie</h1>\r\n          <div class="line"></div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n\t')
        __M_writer(str( self.body() ))
        __M_writer('\r\n\r\n\r\n  </div>\r\n  \r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/template.html", "uri": "template.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 83, "24": 83, "30": 24}}
__M_END_METADATA
"""
