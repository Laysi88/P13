# P13 OC Lettings

![Documentation Status](https://readthedocs.org/projects/p13-oc/badge/?version=latest)
![CI](https://github.com/Laysi88/P13/actions/workflows/ci.yml/badge.svg)
[![Docker Pulls](https://img.shields.io/docker/pulls/laysi88/p13-app.svg)](https://hub.docker.com/r/laysi88/p13-app)



## 🔗 Documentation

La documentation complète du projet est disponible ici :  
👉 [https://p13-oc.readthedocs.io/fr/latest/](https://p13-oc.readthedocs.io/fr/latest/)  

## 📦 Installation, déploiement, et plus...

Ce projet est développé dans le cadre du parcours Développeur Python d'OpenClassrooms.  

### ✅ Prérequis

- Python 3.12
- Docker
- Git

### ⚙️ Installation sous Windows

1. **Cloner le repository**  
```bash
git clone https://github.com/Laysi88/P13
```
2. **Créer un environnement virtuel**  
```bash
python -m venv env 
 ```

3. **Activer l'environnement virtuel**
```powershell
.\env\Scripts\Activate.ps1
```
4. **Installer les dépendances**
```bash
pip install -r requirements.txt
``` 
5. **Créer un fichier `.env`** à la racine du projet avec les variables suivantes :
```env
SECRET_KEY=<Clé Django>
SENTRY=<Votre DNS Sentry>
ALLOWED_HOSTS=<Vos hosts autorisés>

```

6. **Exécuter le site** 
```bash
python manage.py runserver
```  

7. **Exécuter Flake8**
```bash
flake8 .
```  
8. **Exécuter Pytest + cov**
```bash
pytest --cov=. 
``` 

### ⚙️ Installation sous Docker

1. **Créer un dossier** 

2. **Créer un fichier `.env`** à la racine du projet avec les variables suivantes :
```env
SECRET_KEY=<Clé Django>
SENTRY=<Votre DNS Sentry>
ALLOWED_HOSTS=<Vos hosts autorisés>
```

3. **Lancer la commande:**
```bash
docker run --pull always --env-file .env -p 8000:8000 -d laysi88/p13-app
``` 
Celle-ci téléchargera la dernière version de l'image sur Docker Hub,créera le conteneur,injectera les variables d'environnement depuis le .env,exposera l'application sur localhost:8000 et démarrera le conteneur en arrière plan

4. **Accéder au site depuis http://localhost:8000/**

### 🛠️ Panel d'administration Django

Accédez à l'interface d'administration pour gérer les données du site :

🌐 **URL** : [http://localhost:8000/admin](http://localhost:8000/admin)  
🔑 **Identifiants par défaut** :
- **Utilisateur** : `admin`
- **Mot de passe** : `Abc1234!`