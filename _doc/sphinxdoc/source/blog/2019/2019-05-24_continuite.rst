
.. blogpost::
    :title: Réseau de neurones profond et continu
    :keywords: magnitude
    :date: 2019-05-24
    :categories: densité

    C'est une idée qui me trottait dans la tête.
    Pourquoi les réseaux de neurones profonds fonctionnent
    si bien ? Pourquoi un grand nombre de couches fonctionne-t-il
    mieux qu'une simple couche alors même qu'on sait prouver que
    celle-ci peut approximer n'importe quelle fonction
    continue d'un convexe à valeur dans un convexe ?
    `Démonstration du théorème de la densité des réseaux de neurones
    <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/rn/rn_4_densite.html>`_.

    Une piste de recherche qui me venait à l'esprit était de représenter
    le problème comme une problème de transfert continu depuis
    les entrées vers la sortie en supposant que ce transfer en contraint
    par des bornes sur le gradient. En gros, le réseau de neurones
    profond est maintenant une cube dense, conne si c'était
    le passage à la limite d'un nombre croissant de couches.
    Une couche correspond à une coupe de ce cube, une sorte
    d'arrêt sur images lors du transfert.

    L'idée est que ce type de structure a moins d'optima locaux
    qu'un nombre discret de couche. En quelque sorte,
    un réseau de neurones profond et infini résoud un problème
    de morphisme ou un problème de transport optimal.

    Bref, je ne suis pas le seul à avoir une tell idée :
    `Transport Analysis of Infinitely Deep Neural Network
    <http://www.jmlr.org/papers/v20/16-243.html>`_.
