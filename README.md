IndieGogo clone
===============

Vincent / Emmanuel / Bettina

## Utilisation de c9.io pour travailler sur le projet

En résumé :

- créer un compte sur c9.io (utiliser votre compte github)
- exporter votre clef ssh c9.io vers github
  - copier votre clef (dans le dashboard de c9.io, le lien "show your ssh key"
  - sur github.com, en étant connecté, l'icône "outils" en haut à gauche
  - sélectionner SSH Keys
  - cliquer sur ADD SSH KEY, donner un titre et copier la clef dans le champ key
- créer un nouvel environnement de travail (CUSTOM ou bien PYTHON/DJANGO)
- ouvrir cet environnement
- dans le terminal, cloner votre projet **en utilisant le lien ssh** (`git clone git@github.com:/ISNTeamDumezil/NOMDUPROJET`)
- travailler sur un ou plusieurs fichiers, en créer des nouveaux, etc..
- à la fin de la session de travail : `git status`, `git add FICHIERSMODIFIES`, `git commit`, `git push`