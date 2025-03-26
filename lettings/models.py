"""
Models related to the lettings application.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a postal address.

    Attributes:
        number (PositiveIntegerField): Street number (max 9999).
        street (CharField): Street name.
        city (CharField): City name.
        state (CharField): Two-letter state code.
        zip_code (PositiveIntegerField): ZIP code (max 99999).
        country_iso_code (CharField): ISO 3-letter country code.

    Meta:
        db_table (str): Name of the database table used by Django.
        verbose_name_plural (str): Custom plural name for the admin interface.

    Methods:
        __str__(): Returns the formatted address string.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        db_table = "oc_lettings_site_address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Returns:
            str: Formatted address (e.g., "123 Main St").
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Represents a rental listing.

    Attributes:
        title (CharField): Title of the letting.
        address (OneToOneField): Linked address.

    Meta:
        db_table (str): Name of the database table used by Django.
        verbose_name_plural (str): Custom plural name for the admin interface.

    Methods:
        __str__(): Returns the title of the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = "oc_lettings_site_letting"
        verbose_name_plural = "Lettings"

    def __str__(self):
        """
        Returns:
            str: The title of the letting.
        """
        return self.title
