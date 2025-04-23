Interfaces de programmation
===========================

Vues principales
----------------

- **Page d’accueil**  
  - URL : `/`  
  - Vue : `oc_lettings_site.views.index`  
  - Description : Affiche la page d’accueil de l’application.

- **Liste des locations**  
  - URL : `/lettings/`  
  - Vue : `lettings.views.index`  
  - Description : Affiche la liste de toutes les locations.

- **Détail d’une location**  
  - URL : `/lettings/<int:letting_id>/`  
  - Vue : `lettings.views.letting`  
  - Description : Affiche les détails d’une location spécifique.

- **Liste des profils utilisateurs**  
  - URL : `/profiles/`  
  - Vue : `profiles.views.index`  
  - Description : Affiche la liste des profils utilisateurs.

- **Détail d’un profil utilisateur**  
  - URL : `/profiles/<str:username>/`  
  - Vue : `profiles.views.profile`  
  - Description : Affiche les détails d’un utilisateur donné.

Gestion des erreurs
-------------------

- **Erreur 404 – Page introuvable**  
  - Vue : `oc_lettings_site.views.error_404_view`  
  - Description : Vue personnalisée pour afficher une page 404.

- **Erreur 500 – Erreur serveur**  
  - Vue : `oc_lettings_site.views.error_500_view`  
  - Description : Vue personnalisée pour afficher une page 500.



