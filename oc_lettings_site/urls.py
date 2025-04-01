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


def trigger_error(request):
    """Trigger an error for testing purposes."""
    return 1 / 0


handler404 = "oc_lettings_site.views.error_404_view"
handler500 = "oc_lettings_site.views.error_500_view"

urlpatterns = [
    path("sentry-debug/", trigger_error),
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]
