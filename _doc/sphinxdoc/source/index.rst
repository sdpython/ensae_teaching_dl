
.. |gitlogo| image:: _static/git_logo.png
             :height: 20

Découverte du deep learning
===========================

Lectures, notebooks, helpers pour faire du :epkg:`deep learning`
ou :epkg:`apprentissage profond` sous :epkg:`Python`.
Le deep learning signifie aussi des calculs intensifs et des modules qui
utilisent un compilateur :epkg:`C++` pour optimiser les calculs
et le :epkg:`GPU` si vous en avez.

.. toctree::
    :maxdepth: 1

    lectures_exos
    chapters/index
    gpu
    api/index
    i_ex
    all_notebooks
    i_index

Vous pouvez exécuter la fonction
:func:`pyopencl_status <ensae_teaching_dl.faq.faq_gpu.pyopencl_status>`
pour obtenir plus d'information sur les processeurs disponibles.

Si :epkg:`tensorflow` reste sans doute le framework
de deep learning le plus utilisé, beaucoup de chercheurs
et professeurs utilisent soit :epkg:`keras`, soit
epkg:`torch` et le dernier est le plus plébiscité
par les chercheurs. L'installation est simple et
la documentation est très bien faite, le code
est souvent plus intuitif. Son point faible est encore
la mise en production de modèles, :epkg:`tensorflow` est
plus avancé sur ce point. :epkg:`ONNX` et :epkg:`onnxruntime`
est l'option choisie par :epkg:`pytorch` qui n'est pas le
seul framework à suivre cette direction.

`github <https://github.com/sdpython/ensae_teaching_dl/>`_,
`documentation <http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/index.html>`_,
:ref:`l-README`,
:ref:`blog <ap-main-0>`

.. image:: https://travis-ci.com/sdpython/ensae_teaching_dl.svg?branch=master
    :target: https://app.travis-ci.com/github/sdpython/ensae_teaching_dl
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/b7c2o4fqlaxl0r0a?svg=true
    :target: https://ci.appveyor.com/project/sdpython/ensae-teaching-dl
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/ensae_teaching_dl/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/ensae_teaching_dl/tree/master

.. image:: https://badge.fury.io/py/ensae_teaching_dl.svg
    :target: https://pypi.org/project/ensae_teaching_dl/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://codecov.io/github/sdpython/ensae_teaching_dl/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/ensae_teaching_dl?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/ensae_teaching_dl.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/ensae_teaching_dl/issues

.. image:: nbcov.png
    :target: http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

.. image:: https://img.shields.io/github/repo-size/sdpython/ensae_teaching_dl
    :target: https://github.com/sdpython/ensae_teaching_dl/
    :alt: size

+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`l-modules`     |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods`   | :ref:`l-staticmethods` | :ref:`l-properties`                            |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`modindex`      |  :ref:`l-EX2`       | :ref:`search`       | :ref:`l-license`   | :ref:`l-changes`       | :ref:`l-README`                                |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`genindex`      |  :ref:`l-FAQ2`      | :ref:`l-notebooks`  | :ref:`l-HISTORY`   | :ref:`l-statcode`      | `Unit Test Coverage <coverage/index.html>`_    |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
