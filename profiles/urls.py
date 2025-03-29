"""
URL configuration for the profiles application.

This module defines the URL patterns related to user profiles, including:
- Listing all profiles.
- Viewing the details of a specific user profile by username.

Routes:
    /profiles/                    → Display all user profiles.
    /profiles/<str:username>/    → Display details of a specific user profile.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="profiles_index"),
    path("<str:username>/", views.profile, name="profile"),
]
