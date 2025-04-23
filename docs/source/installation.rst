Instructions d’installation
===========================

Cette section explique comment installer et configurer l'application **P13 OC Lettings** en local.

Prérequis
---------

- Python 3.10 ou supérieur
- `pip` (installé avec Python)
- Git (optionnel mais recommandé)
- Un environnement virtuel Python (`venv` ou `virtualenv`)

Étapes d'installation
---------------------

1. **Cloner le dépôt :**

   .. code-block:: bash

      git clone https://github.com/Laysi88/P13  
      cd P13

2. **Créer un environnement virtuel :**

   .. code-block:: bash

      python -m venv env
      env\Scripts\activate  # Windows
      source env/bin/activate  # Linux/MacOS

3. **Installer les dépendances :**

   .. code-block:: bash

      pip install -r requirements.txt

4. **Configurer l'application :**

   - Créer un fichier `.env` à la racine du projet.
   - Ajouter les variables d'environnement nécessaires dans le fichier `.env`.
   - Exemple de configuration :

     .. code-block:: bash

        SECRET_KEY=your_secret_key  
        ALLOWED_HOSTS=localhost  
        SENTRY_DSN=your_sentry_dsn

5. **Appliquer les migrations :**

   .. code-block:: bash

      python manage.py migrate

6. **Lancer le serveur :**

   .. code-block:: bash

      python manage.py runserver

Vous pouvez maintenant accéder à l'application à l'adresse : `http://localhost:8000`
