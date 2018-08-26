# -*- coding: utf-8 -*-
import sys
import os
# import sphinx_redactor_theme
# import karma_sphinx_theme
import sphinx_bootstrap_theme
from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet


sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
local_template = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "phdoc_templates")

set_sphinx_variables(__file__, "ensae_teaching_dl", "Xavier Dupré", 2018,
                     "bootstrap", sphinx_bootstrap_theme.get_html_theme_path(),
                     locals(), extlinks=dict(
                         issue=('https://github.com/sdpython/ensae_teaching_dl/issues/%s', 'issue')),
                     title="ensae_teaching_dl", book=True)

if False:
    html_sidebars['**'] = ['globaltoc.html', 'localtoc.html', 'relations.html',
                           'sourcelink.html', 'searchbox.html']
    html_sidebars['*'] = html_sidebars['**']
    html_sidebars[''] = html_sidebars['*']

html_theme_options = {
    'touch_icon': '_static/project_ico.ico',
}

blog_root = "http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/"

html_context = {
    'css_files': get_default_stylesheet() + ['_static/my-styles.css', '_static/gallery.css'],
}


html_logo = "project_ico.png"

language = "fr"

mathdef_link_only = True

epkg_dictionary['apprentissage profond'] = 'https://fr.wikipedia.org/wiki/Apprentissage_profond'
epkg_dictionary['deep learning'] = 'https://en.wikipedia.org/wiki/Deep_learning'
epkg_dictionary['ENSAE'] = 'http://www.ensae.fr/'
epkg_dictionary['GIL'] = 'http://www.xavierdupre.fr/app/teachpyx/helpsphinx/notebooks/gil_example.html'
epkg_dictionary['itérateur'] = 'https://fr.wikipedia.org/wiki/It%C3%A9rateur'
epkg_dictionary['map/reduce'] = 'https://fr.wikipedia.org/wiki/MapReduce'
epkg_dictionary['numba'] = 'https://numba.pydata.org/'
epkg_dictionary['pytorch'] = 'https://pytorch.org/'
epkg_dictionary['sqlite3'] = "https://docs.python.org/3.6/library/sqlite3.html"
epkg_dictionary['SQL'] = 'https://fr.wikipedia.org/wiki/Structured_Query_Language'
