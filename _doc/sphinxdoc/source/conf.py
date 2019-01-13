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

set_sphinx_variables(__file__, "ensae_teaching_dl", "Xavier Dupré", 2019,
                     "bootstrap", sphinx_bootstrap_theme.get_html_theme_path(),
                     locals(), extlinks=dict(
                         issue=('https://github.com/sdpython/ensae_teaching_dl/issues/%s', 'issue')),
                     title="ensae_teaching_dl", book=True)

if False:
    html_sidebars['**'] = ['globaltoc.html', 'localtoc.html', 'relations.html',
                           'sourcelink.html', 'searchbox.html']
    html_sidebars['*'] = html_sidebars['**']
    html_sidebars[''] = html_sidebars['*']

if html_theme == "bootstrap":
    html_theme_options = {
        'navbar_title': ".",
        'navbar_site_name': "Site",
        'navbar_links': [
            ("XD", "http://www.xavierdupre.fr", True),
        ],
        'navbar_sidebarrel': True,
        'navbar_pagenav': True,
        'navbar_pagenav_name': "Page",
        'bootswatch_theme': "readable",
        # united = weird colors, sandstone=green, simplex=red, paper=trop bleu
        # lumen: OK
        # to try, yeti, flatly, paper
        'bootstrap_version': "3",
        'source_link_position': "footer",
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
epkg_dictionary['Tensorflow'] = 'https://www.tensorflow.org/'
epkg_dictionary['TensorFlow'] = 'https://www.tensorflow.org/'
