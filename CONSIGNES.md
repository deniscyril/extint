# Consignes pour ce projet

(ne pas supprimer ni modifier ce fichier SVP)

## Séance du 21 février
* Etape 1 : trouver le sujet
* Etape 2 : réfléchir aux structures de données à traiter

## Séance du 14 mars
- puller le dépôt (indice : git pull)
- écrire un fichier AUTHORS contenant vos noms, prénoms et 
  adresses email (une par ligne)
- créer des mockups (un schema grossier) des différentes vues
  envisageables dans le programme (EN ETANT RAISONNABLE !!!!!!), 
  logiciels utilisables : dia ou inkscape
- enregistrer ces mockups dans un dossier *mockups* en nommant
  chaque fichier par le titre de la vue
- ajouter, commiter et pousser (indice : git gui ou bien git add,
  git commit, git push)

## Séance du 21 mars
- préparer un espace de travail sur c9.io en suivant les consignes contenue
  dans README.md et vérifier que vous pouvez travailler avec. Vous pourrez
  ensuite travailler pour la suite sur c9 OU sur votre clef (attention 
  le réseau du lycée est pourri)...
- git status // git pull
- faire le fichier AUTHORS (ci-dessus)
- compléter le mockup par les vues "secondaires" manquantes (réfléchir à la
  destination de chaque action / chaque clic sur les pages proposées)
- commencer à réfléchir aux structures de données à utiliser côté serveur
  pour pouvoir réaliser le site
- git commit // git pull // git push

## Séance du 28 mars
- définir les structures de données à utiliser côté serveur
- définir à partir du mockup les différentes vues à créer ainsi que
  les données associées (données nécessaires pour afficher la page, et 
  données transmises par la page -> destination)

## Séances du 4 avril et du 11 avril
- Emmanuel : faire le ménage dans le répertoire Site 
  (ne pas commiter les virtualenv, isoler le python, voir .gitignore..)
- Vincent : faire pour chaque page un modèle des données reçues et envoyées
  en YAML 
- Bettina + Vincent : commencer à construire les pages html des templates
  - lire documentation templates django
  - écrire template "de base" + feuille de style

## Séance du 18 avril
- Vincent / Bettina : continuer l'écriture des templates
- Emmanuel : implémenter les vues de base