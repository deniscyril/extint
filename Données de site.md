##### Le 29 mars 2014
##### Salle A 200

# « Données associées »


##### 	Ce document compile les différentes données qui vont être demandées par le site, ainsi que celles qui vont être envoyées par celui-ci ; et ce pour chaque page du site. Chaque page de ce document contient la liste des rubriques de chaque page du site, avec, classées par « Données demandées » et « Données envoyées », les données associées à chaque rubrique.


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
- Mot de passe utilisateur en 6 caractères minimum (caractères alphanumériques + symboles)
- Pression du bouton « Connexion », une fois les deux champs ci-dessus complétés

####	 Données envoyées :

- Renvoi vers la page « Interface donateur », sur le compte de l'utilisateur
- Saisie incorrecte ...
- Afficher « Verrouillage majuscule actif » si la touche CAPS LOCK est active, durant la saisie du mot de passe
- Aucun renvoi, si absence de clic sur le bouton « Connexion » ou si page chargée depuis plus de 2 minutes
- Défilement d'informations dans le cadre du bas appelé « Photo » : photo enthousiaste, statistiques du site, publicité


### « Liste des projets » :


#### 	Données demandées :

- Action de l'utilisateur : clic sur un ensemble « Image + texte projet x »


####	 Données envoyées :

- Renvoi vers la page « Liste des projets »
- Aucune, si absence de clic


### 	Interface entrepreneur :


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


### Projet [X] :


####	Données demandées :

- Vérification transparente faite par le site si un utilisateur est connecté
- Valeur chiffrée d'un investissement (caractères numériques)
- Confirmation de la demande d'investissement (case « Confirmer » cochée)
- Pression du bouton « Investir », une fois les champs ci-dessus complétés


#### 	Données envoyées :


- Séparation des milliers lors de la saisie d'une valeur
- Affichage des champs "Valeur de l'investissement" et la case "Confirmer" SEULEMENT si un utilisateur est connecté.
  - Sinon afficher "Il faut être connecté pour investir. Créez un compte ou inscrivez-vous !"
- Affichage du bouton "Retour à l'interface" SEULEMENT si un utilisateur est connecté :
  - Retour à l'interface de l'utilisateur si ce bouton est cliqué
- Si les champs ci-dessus tous complétés, afficher le message « Félicitations ! ». Pas de renvoi vers une page et proposer "Vous pouvez décider de continuer à investir, regarder des projets, ou retourner à votre espace personnel".
- Si une valeur non numérique est entrée : afficher le message « Saisie incorrecte : seuls des chiffres peuvent être entrés " ; et effacer la saisie
- Si la confirmation est remplie, dégriser le bouton « Investir »


--------------------------------------------------------------------------

## Interface donateur 


### Remarque importante : cette page ne s'affiche que si l'utilisateur est connecté. Cette page demande donc les données suivantes d'office ; qui seront matérialisées par un cookie :

- Nom d'utilisateur
- Mot de passe

### S'affiche alors la page, considérée ici en tant qu'ensemble de données.

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

### Coordonées financières :


#### Données demandées :


- Vérification par le site si un carte bancaire déjà enregistrée ou non. 

###### Si oui, voir données envoyées

- Numéro de carte bancaire, composée de 4 ensembles de quatre chiffres. 
- Cryptogramme de la carte, composé de 1 ensemble de 3 chiffres
- Nom souhaité par l'utilisateur pour désigner sa carte (caractères alphanumériques + symboles)


#### Données envoyées :


- Coordonnées de la carte bancaire déjà enregistrée + nom de la carte :
  - Numéro de carte, dont les 3 derniers ensemble de chiffres seront grisés
  - Etablissement bancaire auquel est rattaché la carte
  - Nom défini par l'utilisateur pour la carte
- Lorsque le champs "Numéro de carte" est correctement rempli, séparer dès lors qu'un groupe de 4 chiffres est entré, le nouveau groupe par un espace double.
- Si les 3 champs "Numéro de carte", "Cryptogramme" et "Nom" sont correctement remplis, afficher "La carte a été ajoutée" ainsi que les coordonnées de la nouvelle carte associée à son nom.
- Si le champs "Numéro de carte bancaire" comporte un caractère non numérique : 
  - Effacer celui-ci
  - Afficher "seuls des chiffres peuvent être entrés"
- Si le champs "Numéro de carte" comporte plus ou moins de 16 chiffres :
  - Afficher "Erreur : un numéro de carte est composé de 16 chiffres. Un ou plusieurs chiffres sont soit de trop, soit manquants."
  - Colorer en rouge le champ "Numéro de carte" jusqu'à ce que le champ ne contienne que 16 chiffres
- Si le champs "Cryptogramme" comporte un caractère non numérique :
  - Refuser la saisie
  - Simulatnément afficher "Seuls des chiffres peuvent être entrés
- Si le champs "Cryptogramme" comporte plus de 3 chiffres :
  - Afficher "Erreur : un cryptogramme ne contient que 3 chiffres. Un ou plusieurs chiffres sont soit de trop, soit manquants."
 -  Colorer en rouge le champ "Cryptogramme" jusqu'à ce qu'il ne contienne que 3 chiffres.
- Si le champs "Etablissement bancaire" est laissé vide :
  - Colorer en rogue le camps jusqu'à ce qu'il soit correctement complété
  - Afficher "Une carte bancaire doit être reliée à un établissement bancaire"
- Si le champs "Nom de la carte est laissé vide" :
  - Afficher "Êtes-vous sûr de ne pas vouloir nommer votre carte ? Ceci n'est pas indispensable à la poursuite de la saisie"
 - Nommer ensuite cette carte "Carte numéro 1"

--------------------------------------------------------------------

## 	Interface entrepreneur 

### Remarque importante : cette page ne s'affiche que si l'utilisateur est connecté. Cette page demande donc les données suivantes d'office ; qui seront matérialisées par un cookie :

- Nom d'utilisateur
- Mot de passe

### S'affiche alors la page, considérée ici en tant qu'ensemble de données.

##### 	Cette page comporte les rubriques suivantes : 


- Vos projets
- Création de projet
- "Profil entrepreneur"
- Informations financières ("Montant total")
- Coordonnées bancaires (affichage variable selon qu'on ait entré une seule carte ou plusieurs)

### Vos projets


#### Données demandées :


- Vérification par le site des projets entrepris par l'utilisateur


#### Données envoyées :


- Si aucun projet n'est enregistré, afficher "Vous n'avez entrepris aucun projet. Mais vous êtes libre d'en créer un nouveau !"
- Afficher les 4 derniers projets actuellement en cours de l'utilisateur :
  - Nom du projet
  - Photo associée au projet
  - Description du projet
  - Montant collecté pour le projet


### Création de projet :


#### Données demandées :


- Nom du projet (caractère alphanumériques)
- Photo du projet à uploader
- Montant demandé (chiffres uniquement)
- Description du projet :
  - Contenu
  - Intérêt pour tous
  - Rentabilité espéré (temps avant amortissement, bénéfice, ...)
  - Compétences dans le domaine du projet de l'entrepreneur
- Clic sur "Créer le projet", une fois tous les champs correctement complétés. 


#### Données envoyées :


- Une fois le projet correctement enregistré :
  - Vérification faite par le site si une carte bancaire est enregistrée :
   - Si absence de carte bancaire afficher "Projet refusé : il faut enregistrer une carte bancaire valide"
  - Sinon si une carte existe : 
   - Afficher "[Nom du projet] enregistré"
   - Afficher le projet dans "Vos projets"
- Si le champs "Nom du projet" est vide :
  - Colorer le champs en rouge jusqu'à ce qu'au moins 3 caractères y soit rentrés
  - Afficher "Vous devez saisir un nom pour le projet" 
- Si le champs "Montant demandé" comporte des caractères non numériques :
  - Refuser la saisie
  - Simulatnément afficher "Seuls des chiffres peuvent être entrés


### Profil entrepreneur 


#### Données demandées 


- Description (caractères alphanumériques) 
- CV (Curriculum Vitae) : 
  - en caractères alphanumériques 
  - photo


#### Données envoyées :


- Description entrée par l'utilisateur
- CV entré par l'utilisateur


### Coordonnées financières :


#### Données demandées :


- Numéro de carte bancaire, composée de 4 ensembles de quatre chiffres. 
- Cryptogramme de la carte, composé de 1 ensemble de 3 chiffres
- Nom souhaité par l'utilisateur pour désigner sa carte (caractères alphanumériques + symboles)


#### Données envoyées :


- Coordonnées de la carte bancaire déjà enregistrée + nom de la carte :
  - Numéro de carte, dont les 3 derniers ensemble de chiffres seront grisés
  - Etablissement bancaire auquel est rattaché la carte
  - Nom défini par l'utilisateur pour la carte
- Lorsque le champs "Numéro de carte" est correctement rempli, séparer dès lors qu'un groupe de 4 chiffres est entré, le nouveau groupe par un espace double.
- Si les 3 champs "Numéro de carte", "Cryptogramme" et "Nom" sont correctement remplis, afficher "La carte a été ajoutée" ainsi que les coordonnées de la nouvelle carte associée à son nom.
- Si le champs "Numéro de carte bancaire" comporte un caractère non numérique : 
  - Effacer celui-ci
  - Afficher "seuls des chiffres peuvent être entrés"
- Si le champs "Numéro de carte" comporte plus ou moins de 16 chiffres :
  - Afficher "Erreur : un numéro de carte est composé de 16 chiffres. Un ou plusieurs chiffres sont soit de trop, soit manquants."
  - Colorer en rouge le champ "Numéro de carte" jusqu'à ce que le champ ne contienne que 16 chiffres
- Si le champs "Cryptogramme" comporte un caractère non numérique :
  - Refuser la saisie
  - Simulatnément afficher "Seuls des chiffres peuvent être entrés
- Si le champs "Cryptogramme" comporte plus de 3 chiffres :
  - Afficher "Erreur : un cryptogramme ne contient que 3 chiffres. Un ou plusieurs chiffres sont soit de trop, soit manquants."
 -  Colorer en rouge le champ "Cryptogramme" jusqu'à ce qu'il ne contienne que 3 chiffres.
- Si le champs "Etablissement bancaire" est laissé vide :
  - Colorer en rogue le camps jusqu'à ce qu'il soit correctement complété
  - Afficher "Une carte bancaire doit être reliée à un établissement bancaire"
- Si le champs "Nom de la carte est laissé vide" :
  - Afficher "Êtes-vous sûr de ne pas vouloir nommer votre carte ? Ceci n'est pas indispensable à la poursuite de la saisie"
 - Nommer ensuite cette carte "Carte numéro 1"

- Après calcul par le site, afficher "Valeur en euros du montant collecté"


--------------------------------------------------------------------------


## Inscription "donateur" #1 // Inscription "entrepreneur" #1


###### Cette page est très similaire à "Inscription "Entrepreneur" #1", donc une seule page résumera leurs données. 

##### Cette page contient les rubriques suivantes : 


- Pseudonyme
- Coordonnées


### Pseudonyme :


#### Données demandées :


- Nom (caractères alphabétiques + symboles)
- Prénom (caractères alphabétiques)
- Nom d'utilisateur désiré (caractères alphanumériques + symboles)
- Mot de passe (caractères alphanumériques + symboles)
- Date de naissance


#### Données envoyées : 


- Si tous les champs de toutes les rubriques sont correctement remplis, et que "Etape suivante" a été cliqué, alors afficher INSCRIPTION "DONATEUR" #2
- Si un des champs est laissé vide :
  - Afficher "Erreur : [nom du champs] est vide, il faut qu'il soit rempli"
  - Colorer en rouge le [champs] vide
- Si un champs est incorrecement rempli :
  - Présence d'un caractère numérique dans "Nom", "Prénom", ou de plus de 2 espaces consécutifs :
   - Afficher "Seuls des caractères alphabétiques ou éventuellement des symboles peuvent être entrés" s'il s'agit de caractères erronés
   - Refuser la saisie dans tous les cas
  - Présence d'un caractère alphabtéique dans "Année" , ou de plus de 4 chiffres :
   - Afficher "Seuls des chiffres peuvent être entrés" s'il s'agit de caractères non numériques
   - Refuser la saisie dans tous les cas


### Coordonnées : 


#### Données demandées :


- Pays de résidence 
- Adresse mail
- Numéro de téléphone principal (caractères numériques + {+}"
- Numéros de téléphone supplémentaire (optionnels)


#### Données envoyées :


- Si tous les champs de toutes les rubriques sont correctement remplis, et que "Etape suivante" a été cliqué, alors afficher INSCRIPTION "ENTREPRENEUR" #2
- Si un des champs est laissé vide :
  - Afficher "Erreur : [nom du champs] est vide, il faut qu'il soit rempli"
  - Colorer en rouge le [champs] vide
- Si un champs est incorrecement rempli :
  - Si le champs "Adresse mail" comporte une adresse non valide (pas de @, pas de .com) : 
   - Afficher "Une adresse s'exprime ainsi : {adresse@fournisseur.pays} "
   - Colorer le champs en rouge
  - Si le champs "Numéro de téléphone [...] comporte des caractères non numériques :
   - Afficher "Seuls des chiffres peuvent être entrés"
   - Refuser la saisie

---------------------------------------------------------------------------


## Inscription "donateur" #2 // Inscription "entrepreneur" #2


###### Cette page est très similaire à "Inscription "Entrepreneur" #1", donc une seule page résumera leurs données. 

##### Cette page contient les rubriques suivantes : 


- Accord avec les conditions d'utilisations


#### Données demandées : 


- "cochage" d'une des cases
- Clic sur "Valider l'inscription"


#### Données envoyées :


- Si la case "J'accepte les conditions d'utilisations" est cochée, et que "Valider l'inscription" est cliqué ; afficher "Félicitations, vous êtes désormais un [donateur/entrepreneur]"
- Si la case "Je refuse les conditions d'utilisations du site" est cochée, griser "Valider l'inscription" et afficher "Vous devez accepter les conditions d'utilisations du site pour vous inscrire. Vous pouvez toujours choisir d'accepter les conditions d'utilisations du site et alors pouvoir valider votre inscription"
- Si aucune case est cochée, griser "Valider l'inscription"






