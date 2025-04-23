Description du projet
=====================

**P13 OC Lettings** est une application web développée dans le cadre du projet 13 du parcours Développeur d’Applications Python chez OpenClassrooms.

Fonctionnalités principales
---------------------------

- Visualisation d’une liste de locations
- Consultation du détail d’une location
- Visualisation d'une liste de profiles
- Consultation du détail d'un profile
- Administration de la base de données via l’interface Django Admin
- Journalisation des erreurs et surveillance via Sentry
- Déploiement sur un environnement cloud (Render)

Architecture générale
---------------------

Le projet est composé de trois modules principaux :

- `oc_lettings_site` : point d’entrée de l’application (configuration Django, routes principales, gestion des erreurs)
- `lettings` : module dédié aux annonces immobilières
- `profiles` : module dédié aux utilisateurs et à leur ville de résidence préférée

Ce découpage modulaire permet de faciliter la maintenance et l’évolutivité du projet.