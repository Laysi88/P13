"""
Models related to the profiles application.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile.

    Attributes:
        user (OneToOneField): Reference to Django's built-in User model.
        favorite_city (CharField): User's favorite city (optional).

    Meta:
        db_table (str): Name of the database table used by Django.
        verbose_name_plural (str): Custom plural name for the admin interface.

    Methods:
        __str__(): Returns the username linked to the profile.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        db_table = "oc_lettings_site_profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        """
        Returns:
            str: The username linked to this profile.
        """
        return self.user.username
