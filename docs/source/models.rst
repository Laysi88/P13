Base de données et models
=========================

Base de données
----------------

L'application utilise une base de données relationnelle pour stocker les informations sur les utilisateurs, les annonces et les adresses. Le modèle de données est conçu pour être extensible et facile à maintenir.
La base de données est de type SQlite.
La base de données est gérée par Django ORM, ce qui permet d'interagir avec la base de données à l'aide d'objets Python plutôt que de requêtes SQL brutes.

Models
------
Ce diagramme présente la structure des données de l'application.

.. mermaid::

   classDiagram
     class User

     class Profile {
       +user: User (OneToOne)
       +favorite_city: str
     }

     class Address {
       +number: int
       +street: str
       +city: str
       +state: str
       +zip_code: str
       +country_iso_code: str
     }

     class Letting {
       +title: str
       +address: Address (OneToOne)
     }

     Profile --> User
     Letting --> Address
