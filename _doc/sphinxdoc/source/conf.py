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

epkg_dictionary.update({
    'apprentissage profond': 'https://fr.wikipedia.org/wiki/Apprentissage_profond',
    'auto-keras': 'https://autokeras.com/',
    'chainer': 'https://chainer.org/',
    'cupy': 'https://cupy.chainer.org/',
    'deep learning': 'https://en.wikipedia.org/wiki/Deep_learning',
    'ENSAE': 'http://www.ensae.fr/',
    'GIL': 'http://www.xavierdupre.fr/app/teachpyx/helpsphinx/notebooks/gil_example.html',
    'itérateur': 'https://fr.wikipedia.org/wiki/It%C3%A9rateur',
    'keras': 'https://keras.io/',
    'map/reduce': 'https://fr.wikipedia.org/wiki/MapReduce',
    'numba': 'https://numba.pydata.org/',
    'pycuda': 'https://documen.tician.de/pycuda/',
    'pytorch': 'https://pytorch.org/',
    'sqlite3': "https://docs.python.org/3.6/library/sqlite3.html",
    'SQL': 'https://fr.wikipedia.org/wiki/Structured_Query_Language',
    'Tensorflow': 'https://www.tensorflow.org/',
    'TensorFlow': 'https://www.tensorflow.org/',
    'tvm': 'https://docs.tvm.ai/index.html',
})
