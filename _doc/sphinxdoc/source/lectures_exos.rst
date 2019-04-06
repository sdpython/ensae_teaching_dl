
=======================================
Découvrir le deep learning en exercices
=======================================

Les notebooks utilisent principalement
:epkg:`pytorch` car la lecture du code décrivant un
réseaux de neurones est une des plus intuitives.
Elle est beaucoup moins *verbeuse* que celle de
:epkg:`tensorflow` et offre plus de liberté dans la
conception d'un modèle de deep learning. C'est ce qui
a séduit de nombreux chercheurs à l'utiliser d'autant plus
cette liberté ne s'est pas faite au détriment des performances.
:epkg:`pytorch` supporte également le standard :epkg:`ONNX`
ce qui facilite la mise en production de modèles.

.. contents::
    :local:

Premier pas avec pytorch
========================

.. toctree::
    :maxdepth: 2

    notebooks/100_Logistic_IRIS
    notebooks/110_Perceptron_Iris
    notebooks/200_Perceptron_MNIST
    notebooks/210_Convolution_MNIST
    notebooks/300_Convolution_CIFAR10
    notebooks/400_backward

Tous les notebooks excepté le premier
ont été écrits par
`Matthieu Bizien <http://tantion.com/>`_.

Autres sources de notebooks
===========================

* `tutoriels de pytorch <https://pytorch.org/tutorials/>`_
* `Deep Learning course: lecture slides and lab notebooks <https://github.com/m2dsupsdlclass/lectures-labs>`_
  (master DataScience Université Paris Saclay)
* `Réaliser un moteur de recherche d'images avec du deep learning
  <http://www.xavierdupre.fr/app/mlinsights/helpsphinx/all_notebooks.html#exploration>`_
