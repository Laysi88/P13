"""
Main URL configuration for the Django project.

This module defines the global URL routing for the application,
including the homepage, the admin site, and the included apps: lettings and profiles.

Routes:
    /               → Homepage of the site.
    /lettings/      → URLs from the lettings application.
    /profiles/      → URLs from the profiles application.
    /admin/         → Django admin interface.
"""

from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]
