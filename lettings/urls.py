"""
URL configuration for the lettings application.

This module defines the URL patterns related to lettings, including:
- Listing all lettings.
- Viewing the details of a single letting by its ID.

Routes:
    /lettings/                → Display all lettings.
    /lettings/<int:letting_id>/ → Display details of a specific letting.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="lettings_index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
