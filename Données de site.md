##### Le 29 mars 2014
##### Salle A 200

# « Données associées »


##### 	Ce document compile les différentes données qui vont être demandées par le site, ainsi que celles qui vont être envoyées par celui-ci ; et ce pour chaque page du site. Chaque page de ce document contient la liste des rubriques de chaque pagedu site, avec, classées par « Données demandées » et « Données envoyées », les données associées à chaque rubrique.


- Liste des pages
- Accueil
- Liste des projets
- Interface « Donateur »
- Interface « Entrepreneur »
- Inscription « Donateur » #1
- Inscription « Donateur » #2
- Inscription « Entrepreneur » #1
- Inscription « Entrepreneur » #2


##	 Page accueil :


##### 	Cette page comporte les rubriques suivantes :

- Interface donateur
- « Liste des projets »
- Interface entrepreneur


###	 Interface donateur :


#### 	Données demandées :

- Nom utilisateur (caractère alphanumériques)
- Mot de passe utilisateur (caractères alphanumériques + symboles)
- Pression du bouton « Connexion », une fois les deux champs ci-dessus complétés

####	 Données envoyées :

- Renvoi vers la page « Interface donateur », sur le compte de l'utilisateur
- « Verrouillage majuscule actif » si la touche CAPS LOCK est active, durant la saisie du mot de passe
- Aucun renvoi, si absence de clic sur le bouton « Connexion » ou si page chargée depuis plus de 2 minutes
- Défilement d'informations dans le cadre du bas appelé « Photo » : photo enthousiaste, statistiques du site, publicité


### « Liste des projets » :


#### 	Données demandées :

- Action de l'utilisateur : clic sur un ensemble « Image + texte projet x »


####	 Données envoyées :

- Renvoi vers la page « Liste des projets »
- Aucune, si absence de clic


### 	Interface donateur :


#### 	Données demandées :

- Nom d'utilisateur (caractères alphanumériques)
- Mot de passe utilisateur (caractères alphanumériques + symboles)
- « Verrouillage majuscule actif » si la touche CAPS LOCK est active, durant la saisie du mot de passe
- Pression du bouton « Connexion », une fois les deux champs ci-dessus complétés

#### 	Données envoyées :

- Renvoi vers la page « Interface entrepreneur », sur le compte de l'utilisateur
- Aucun renvoi, si absence de clic sur le bouton « Connexion », ou si page chargée depuis plus de 2 minutes
- Défilement d'informations dans le cadre du bas appelé « Photo » : photo enthousiaste, statistiques du site, publicité

----------------------------------------------------------------------------------------

## 	Liste des projets


##### 	Cette page contient quatre rubriques toutes identiques, que l'on résumera ainsi :


- Projet A
- Projet B
- Projet C
- Projet D


### Projet X :


####	Données demandées :

- Vérification transparente faite par le site si un utilisateur est connecté
- Valeur chiffrée d'un investissement (caractères numériques)
- Confirmation de la demande d'investissement (case « Confirmer » cochée)
- Pression du bouton « Investir », une fois les champs ci-dessus complétés


#### 	Données envoyées :


- Affichage des champs "Valeur de l'investissement" et la case "Confirmer" SEULEMENT si un utilisateur est connecté.
  - Sinon afficher "Il faut être connecté pour investir. Créez un compte ou inscrivez-vous !"
- Affichage du bouton "Retour à l'interface" SEULEMENT si un utilisateur est connecté :
  - Retour à l'interface de l'utilisateur si ce bouton est cliqué
- Si les champs ci-dessus tous complétés, afficher le message « Félicitations ! ». Pas de renvoi vers une page et proposer "Vous pouvez décider de continuer à investir, regarder des projets, ou retourner à votre espace personnel".
- Si une valeur non numérique est entrée : afficher le message « Saisie incorrecte : seuls des chiffres peuvent être entrés " ; et effacer la saisie
- Si la confirmation est remplie, dégriser le bouton « Investir »


--------------------------------------------------------------------------

## Interface donateur 



##### 	Cette page comporte les rubriques suivantes : 


- "Projet à la une"
- Projets soutenus
- Informations financières
- Coordonnées bancaires (affichage variable selon qu'on ait entré une seule carte ou plusieurs)


### 	"Projet à la une"


#### Données demandées :


- Valeur chiffrée d'un investissement (caractères numériques)
- Confirmation de la demande d'investissement (case « Confirmer » cochée)
- Pression du bouton « Investir », une fois les champs ci-dessus complétés

#### 	Données envoyées : 


- Si les champs ci-dessus tous complétés, afficher le message « Félicitations ! ». Pas de renvoi vers une page et proposer "Vous pouvez décider de continuer à investir, regarder des projets, ou voir d'autres projets sur "Liste des projets" .".
- Si une valeur non numérique est entrée : afficher le message « Saisie incorrecte : seuls des chiffres peuvent être entrés " ; et effacer la saisie
- Si la confirmation est remplie, dégriser le bouton « Investir »


### 	Projet soutenus :


#### Données demandées :


- Vérification faite par la site des projets actuellement financés par l'utlisateur.


#### Données envoyées :


- Si des projets ont déjà été financés par un utilisateur, affichage des projets (image + texte) des projets qui ont déjà été financés par l'utilisateur. Afficher les montants investis.
  - Sinon afficher des projets sélectionnés de façon aléatoire

### Informations financières :


#### Données demandées :


- Calcul par le site, à partir des montants investis par l'utilisateur, de l'ensemble des fonds investis par celui-ci.
- Calcul du bénéfice  mensuel espéré à partir des montants des investissements actuels
- Calcul de la durée restante (en mois) de la perception


#### Données envoyées :


- Valeur numériques des fonds investis par l'utilisateur dans le champs "Valeur total du montant en euros"
- Valeur numérique du bénéfice mensuel espéré en euros par l'utilisateur dans le champs "Valeur du bénéfice espéré en euros"
- Valeur numérique de la durée restante de perception (en mois) de la perception par l'utilisateur dans le champs "Durée restante à percevoir"



