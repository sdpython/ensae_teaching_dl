
GPU
===

Le calcul :epkg:`GPU` est étroitement associé
à la réussite du deep learning qui lui doit
des gains en performance significatifs. Le même algorithme
est dix fois plus rapide, voire plus, qu'une version
équivalente :epkg:`CPU`.
La plupart des framework de deep learning propose
une partie de calcul matriciel implémenté en :epkg:`GPU`
via une abstraction appelée :epkg:`tensor` dans la plupart
des librairies.

Librairies de calcul GPU
++++++++++++++++++++++++

Les librairies suivantes ont été développées pour le
deep learning puis ont proposé une extension au calcul
matriciel afin de pouvoir calculer facilement des gradients
sur des architectures de réseaux de neurones personnalisées.

* :epkg:`tensorflow`
* :epkg:`pytorch`
* :epkg:`cupy` (:epkg:`chainer`)

Ces frameworks sont optimisés pour l'apprentissage de réseaux de
neurones et pas nécessairement pour leur utilisation. C'est pourquoi
d'autres librairies ont émergés plus axées sur le calcul rapides
d'une prédiction. C'est le cas d':epkg:`onnxruntime` qui s'intéresse
à la mise en production de modèle de machine learning y compris
deep learning. Cette librairie n'est plus liée au langage
:epkg:`python` et le langage principale est le C/C++.
C'est d'ailleurs le cas des librairies qui vont suivre dont l'objectif
est de faciliter l'écriture de calcul GPU :

* :epkg:`boost-compute`, il faut toujours regarder :epkg:`boost`
  car leur standard de programmation est très élevé ce qui en fait
  une librairie robuste
* :epkg:`tvm` (et :epkg:`tvm-python`)
* :epkg:`tensorrt` (proposé par :epkg:`NVidia`)
* :epkg:`arrayfire` (et :epkg:`arrayfire-python`), cette librairie
  utilise :epkg:`cuda` (lié à :epkg:`NVidia`) mais aussi :epkg:`opencl`
  qui propose une interface bas biveau pour toutes les cartes graphiques.
* :epkg:`thrust` (toujours :epkg:`NVidia`)

:epkg:`halide` s'intéresse à la simplification de l'écriture,
comment écrire un code toujours plus concis sans perdre en performance
tout en prenant en compte la particularité du calcul GPU qui est
la parallélisation.
