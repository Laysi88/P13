import pytest
from django.urls import reverse, resolve
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.fixture
def profile():
    user = User.objects.create_user(username="julien", first_name="Julien", last_name="Dupont")
    profile = Profile.objects.create(
        user=user,
        favorite_city="avenue du parc",
    )
    return profile


@pytest.mark.django_db
def test_profile_username_url(profile):
    path = reverse("profile", kwargs={"username": profile.user.username})
    assert path == f"/profiles/{profile.user.username}/"
    assert resolve(path).view_name == "profile"


@pytest.mark.django_db
def test_model_profile(profile):
    expected_value = "julien"
    assert str(profile) == expected_value
