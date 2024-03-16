# 03_07_2020

Début du projet : création de la page HTML et du CSS, des dossiers Fonts et Images.

Je me base beaucoup sur la mise en page que j'ai réalisé sur le site web-to-print pour commencer. Je reprends les styles que j'avais choisis pour cette version pour constituer une base de travail pour ce livre. Je m'éloignerai de ce style plus tard si j'estime que c'est nécessaire.

J'ai mis en place un format de 150 x 200mm, j'ai trouvé comment afficher les traits de coupe et générer du fond perdu.

Je voulais aussi déjà afficher la grille de ligne de base. Il m'a fallu un peu de temps pour comprendre qu'il fallait aussi modifier le style de l'interface pour que cette grille apparaisse à l'écran.

Après avoir commencé à numéroter les images manuellement, je me suis souvenue que j'avais vu un exemple dans la documentation de Paged.js pour implémenter un compteur automatique et j'ai fait le changement.

# 08_07_2020

Aujourd'hui j'ai commencé à affiner la mise en page des premiers éléments coulés la fois précédente. Je suis revenue particulièrement sur les images des premiers articles. Je trouvais les pages trop vides et le rythme trop systématique en ayant à chaque fois une explication à gauche/une image à droite. J'ai donc replacé les images dans le flux de la page (plutôt que sur des pages nommées). Puis j'ai décidé d'ajouter pour certains enchaînements d'images des sections spéciales, des mises en exergue. En pivotant ces images de -90° j'ai dû chercher comment bien les aligner en inspectant longuement la découpe du flux par Paged.js dans le navigateur.

J'ai pour le moment supprimé le fond blanc des pages dans l'interface pour pouvoir visualiser les pages à fond de couleur comme elles doivent apparaître à l'impression.

J'ai voulu faire un test, afficher une bordure de couleur dans certaines pages nommées. J'ai dû inspecter la structure de la page générée par Paged.js pour trouver comment obtenir ce résultat. J'ai appliqué un fond de couleur aux marges de la page et un fond blanc au corps de la page.

# 09_07_2020

Je me suis attardée sur la mise en page des sections de mise en exergue (captures d'écran pivotées de -90° sur fond vert). Je voulais que sur les pages de gauche, l'image apparaîsse avant sa légende, et sur les pages de droite l'inverse pour avoir un effet de symétrie sur les double pages. J'ai eu un peu de mal à trouver comment positionner ces images pivotées étant donné que l'élément que je voyais dans l'inspecteur ne correspondait pas exactement à l'image telle qu'elle était réellement placée. J'ai tenté d'utiliser un display flex sur les éléments figure pour voir si cela me facilitait la tâche mais ça ne fonctionnait pas comme je voulais. J'ai fini par trouver une solution en jouant sur les margin des images et des légendes.

J'ai travaillé les pages de titre de chaque projet, que j'ai pour le moment mises en bichromie bleu et blanc avec une bordure bleue à la page. Étant donné que je présente différents logiciels et outils dans ce livre, il me semblait intéressant d'afficher sur la page de titre de chaque projet le ou les outils qui y sont utilisés, ainsi qu'une introduction et une illustration de celui-ci. C'est en fait la structure que j'ai appliquée au site web d'origine d'où sont issus mes contenus. Il me semble que certains éléments y étaient intéressants et je les réutilise dans le livre.

# 26_08_2020

En revenant sur le projet après plus d'un mois de pause, il m'est apparu que certaines choses ne fonctionnaient pas bien dans le livre. Je trouvais les pages de titres de projets trop vides alors j'ai décidé d'ajouter des les restructurer et d'ajouter des blocs en jouant avec les propriétés de flexbox des blocs. Pour les projets électroniques je voulais essayer de montrer sur le page de titre les composants qui vont être utilisés dans le projet. Je les place dans un bloc en mode display:flex.

# 30_08_2020

En relisant le contenu du livre, il m'a semblé que les étapes des explications n'étaient pas suffisamment identifiables. J'ai donc décidé d'ajouter un compteur à chaque paragraphe pour marquer les étapes, et en regard du texte de mettre un compteur et une légende à toutes les images pour reprendre ces étapes dans le bon ordre, ce qui me semblait plus logique car les images sont justement des captures d'écran de toutes les étapes à suivre.

J'ai redressé toutes les images qui avaient été pivotées de 90 degrés et ai passé toutes les pages d'images sur fond vert pour les démarquer. Je ne trouvais plus la logique de mettre seulement certaines images en exergue pertinente.

J'ai également décidé d'harmoniser les couleurs du livre :  je trouvais qu'il y avait trop de couleurs différentes. J'ai donc supprimé le bleu des pages de titre et le rose des pages de circuit pour les passer en vert.

# 01_09_2020

Il m'a fallu remettre en place la grille de ligne de base dans le CSS. Je l'avais fait disparaître pour bien visualiser les pages sur fond de couleur, mais comme j'arrive à la mise en page des projets électroniques, j'ai besoin de la grille pour m'aider. Pour ces projets, je mets sur la page de gauche les explications du code, et sur la page de droite le code. Tout l'enjeu est de faire en sorte que chaque explication tombe bien en face du bloc de code auquel elle correspond. C'est en cela que la grille m'aide.

# 02_09_2020

Je continue la mise en page des projets électroniques. Pour chaque projet qui fait appel à un nouveau composant, j'exporte une image PNG du composant depuis Fritzing que je dois bien dimensionner pour l'harmoniser avec les autres sur la page de titre.

J'ai modifié le pas de la grille de ligne de base. Je me suis dit qu'elle pourrait me servir de règle en quelque sorte. Je l'ai calée sur le haut de la page (9mm, ce qui correspond au margin des pages) et l'espacement est de 10mm, comme ça je visualise mieux de combien je dois faire descendre mes blocs de code ou mes explications pour les aligner.

# 05_09_2020

Je continue de couler le contenu. Je pensais avant de commencer le projet que les CSS regions seraient parfaitement indiquées pour obtenir le résultat que je recherchais sur les projets électroniques du livre (sur une double page, d'un côté le code, de l'autre les explications). Mais en le faisant, je me rends compte que cela m'aurait peut-être compliqué la tâche puisque l'overflow des contenus, que ce soit le code ou les explications aurait automatiquement coulé vers d'autres blocs et j'aurais quand-même eu à intervenir manuellement pour découper le contenu des pages de façon cohérente. Avec le système que j'utilise dans Paged.js, j'ai des pages nommées pour les explications et pour le code en face, ce qui fait que je sais précisément quel seront les blocs sur chaque double-page. C'est donc plus de travail dans le coulage du contenu que je dois faire alterner moi-même mais ça convient bien à la mise en page que je veux faire.

Pour ce qui est de bien aligner en hauteur dans la page les explications en face du code, j'y arrive assez facilement grâce à la grille de ligne de base qui me sert de repère.

À la fin de certains projets je place une capture d'écran pleine page du rendu du projet. Pour mettre une image en pleine page j'ai trouvé comme solution de la placer sur une page nommée dont les marges sont à 0, et de mettre des marges négatives à l'image pour qu'elle arrive dans la zone de fond perdu.

# 06_09_2020

J'ai passé beaucoup de temps sur un petit problème : j'ai ajouté dans la mise en page d'un projet une capture d'écran de l'IDE Arduino qui intervient au début du code (c'est une manipulation à faire dans l'IDE avant de scripter), donc je ne pensais pas avoir à créer de page nommée pour ça puisque l'image reste dans le flux du contenu. Je voulais avoir l'image seule sur la page de droite, je lui avais mis comme propriétés page-break-before:always et page-break-after:always, mais le page-break-after n'était pas pris en compte, j'avais toujours le h4 de la page suivante qui restait sur la page. Alors j'ai essayé de le pousser de la page en ajoutant du margin-bottom à l'image et du margin-top au h4 mais ça ne fonctionnait pas, le h4 restait sur la page. Je n'ai toujours pas compris si c'était une propriété de Paged.js qui empêchait cela de fonctionner ou s'il y avait autre chose que je n'avais pas saisi. Mais j'ai fini par régler mon problème en créant une page nommée pour l'image.

# 18_09_2020

Après avoir coulé l'intégralité du contenu je voulais mettre en place des césures car de nombreux drapeaux du texte n'étaient pas très harmonieux. J'ai d'abord essayé avec la fonctionnalité Hyphen en CSS mais elle ne marchait pas en français dans ma version de Chromium. J'ai donc cherché un polyfill pour gérer les césures en Javascript et j'ai fini par tomber sur Hypher. Ne sachant pas vraiment utiliser un serveur Node.js, je me suis dirigée sur la version plugin Jquery de ce polyfill. J'ai dû faire un hook au début de mon document HTML pour que la césure des mots soit appliquée à afterPageLayout (sinon Hypher ne fonctionnait pas). Après quelques réglages sur le nombre de lettres de part et d'autre des césures, j'ai fini les corrections ortho-typographiques par quelques césures manuelles avec des <br/> dans le HTML dans des cas de figures précis (mot de 2 lettres en début de phrase en fin de ligne, drapeau disgrâcieux...). Plus d'autres petits réglages manuels de modification des width de certains blocs (parfois directement dans la propriété style en HTML).
