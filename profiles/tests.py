import pytest
from django.test import Client
from django.urls import reverse, resolve
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.fixture
def profile():
    user = User.objects.create_user(username="fakeuser", first_name="fake", last_name="User")
    profile = Profile.objects.create(
        user=user,
        favorite_city="fake city",
    )
    return profile


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_profile_index_url():
    path = reverse("profiles_index")
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles_index"


@pytest.mark.django_db
def test_user_profile_url(profile):
    path = reverse("profile", kwargs={"username": profile.user.username})
    assert path == f"/profiles/{profile.user.username}/"
    assert resolve(path).view_name == "profile"


@pytest.mark.django_db
def test_model_profile(profile):
    expected_value = "fakeuser"
    assert str(profile) == expected_value


@pytest.mark.django_db
def test_profile_index_view(client, profile):
    response = client.get(reverse("profiles_index"))
    assert response.status_code == 200
    assert "profiles_list" in response.context
    assert len(response.context["profiles_list"]) == 1
    assert response.context["profiles_list"][0] == profile


@pytest.mark.django_db
def test_profile_view(client, profile):
    response = client.get(reverse("profile", kwargs={"username": profile.user.username}))
    assert response.status_code == 200
    assert "profile" in response.context
    assert response.context["profile"] == profile
