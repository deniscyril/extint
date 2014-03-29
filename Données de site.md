# Le 29 mars 2014
## Salle A 200

### « Données associées »


	Ce document compile les différentes données qui vont être demandées par le site, ainsi que celles qui vont être envoyées par celui-ci ; et ce pour chaque page du site. Chaque page de ce document contient la liste des rubriques de chaque du site, avec, classées par « Données demandées » et « Données envoyées », les données associées à chaque rubrique.


	Liste des pages :

Accueil
Liste des projets
- Interface « Donateur »
- Interface « Entrepreneur »
- Inscription « Donateur » #1
  - Inscription « Donateur » #2
  - Inscription « Entrepreneur » #1
  - Inscription « Entrepreneur » #2


Page accueil :


	Cette page comporte les rubriques suivantes :

Interface donateur
« Liste des projets »
Interface entrepreneur


	Interface donateur :


	Données demandées :

Nom utilisateur (caractère alphanumériques)
Mot de passe utilisateur (caractères alphanumériques + symboles)
Pression du bouton « Connexion », une fois les deux champs ci-dessus complétés

	Données envoyées :

Renvoi vers la page « Interface donateur », sur le compte de l'utilisateur
« Verrouillage majuscule actif » si la touche CAPS LOCK est active, durant la saisie du mot de passe
Aucun renvoi, si absence de clic sur le bouton « Connexion » ou si page chargée depuis plus de 2 minutes
Défilement d'informations dans le cadre du bas appelé « Photo » : photo enthousiaste, statistiques du site, publicité


« Liste des projets » :


	Données demandées :

Action de l'utilisateur : clic sur un ensemble « Image + texte projet x »


	Données envoyées :

Renvoi vers la page « Liste des projets »
Aucune, si absence de clic


Interface donateur :


	Données demandées :

Nom d'utilisateur (caractères alphanumériques)
Mot de passe utilisateur (caractères alphanumériques + symboles)
« Verrouillage majuscule actif » si la touche CAPS LOCK est active, durant la saisie du mot de passe
Pression du bouton « Connexion », une fois les deux champs ci-dessus complétés

	Données envoyées :

Renvoi vers la page « Interface entrepreneur », sur le compte de l'utilisateur
Aucun renvoi, si absence de clic sur le bouton « Connexion », ou si page chargée depuis plus de 2 minutes
Défilement d'informations dans le cadre du bas appelé « Photo » : photo enthousiaste, statistiques du site, publicité


Liste des projets


	Cette page contient quatre rubriques toutes identiques, que l'on résumera ainsi :


Projet A
Projet B
Projet C
Projet D


Projet X :


	Données demandées :


Valeur chiffrée d'un investissement (caractères numériques)
Confirmation de la demande d'investissement (case « Confirmer » cochée)
Pression du bouton « Investir », une fois les champs ci-dessus complétés


	Données envoyées :


Si les champs ci-dessus tous complétés, afficher le message « Félicitations ! »
Si une valeur non numérique est entrée :
Afficher le message « Saisie incorrecte : seuls des chiffres peuvent être entrés
Si la confirmation est remplie, dégriser le bouton « Investir »

