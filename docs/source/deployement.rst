Procédure de Déploiement et de Gestion de l’Application
=======================================================


Étapes du pipeline CI/CD
-------------------------

Chaque push sur la branche ``main`` déclenche automatiquement le workflow suivant :

1. **Set up job** : initialisation de l’environnement
2. **Checkout code** : récupération du code source
3. **Set up Python** : définition de la version de Python
4. **Install dependencies** : installation des dépendances
5. **Run flake8** : vérification de la qualité du code via `flake8 .`
6. **Run tests** : exécution des tests unitaires via `pytest`
7. **Login to Docker Hub** : authentification sur Docker Hub
8. **Build Docker image** : construction de l’image Docker
9. **Push image to Docker Hub** : publication de l’image sur Docker Hub

Secrets et variables d’environnement GitHub
-------------------------------------------

Le fichier `.github/workflows/ci.yml` utilise les secrets suivants (configurés dans GitHub `Settings > Secrets and variables > Actions`) :

- ``DOCKER_USERNAME`` : Nom d’utilisateur Docker Hub
- ``DOCKER_PASSWORD`` : Mot de passe Docker Hub
- ``DOCKER_IMAGE_NAME`` : Nom de l’image Docker 
- ``SENTRY_DSN`` : Token de monitoring pour Sentry
- ``SECRET_KEY`` : Clé secrète pour Django


Déploiement sur Render
----------------------

Étapes de déploiement sur Render :

1. Créer un compte sur Render

2. Créer un nouveau service Web

3. Choisir l'image Docker à déployer

4. Configurer les variables d'environnement :

   - ``DOCKER_USERNAME`` : Nom d’utilisateur Docker Hub
   - ``DOCKER_PASSWORD`` : Mot de passe Docker Hub
   - ``DOCKER_IMAGE_NAME`` : Nom de l’image Docker
   - ``SENTRY_DSN`` : Token de monitoring pour Sentry
   - ``SECRET_KEY`` : Clé secrète pour Django

5. Définir le port d'écoute :

   - Port par défaut : ``8000``

6. Lancer le déploiement

7. Surveiller les logs pour s'assurer que le déploiement s'est bien déroulé

8. Accéder à l'application via l'URL fournie par Render
