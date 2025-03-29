import pytest
from django.urls import resolve, reverse
from django.test import Client
from lettings.models import Letting, Address


@pytest.fixture
def address():
    return Address.objects.create(
        number="123",
        street="Main St",
        city="Springfield",
        state="IL",
        zip_code="62704",
        country_iso_code="US",
    )


@pytest.fixture
def letting(address):
    return Letting.objects.create(
        title="Test Letting",
        address=address,
    )


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_address_model(address):
    expected_value = f"{address.number} {address.street}"
    assert str(address) == expected_value


@pytest.mark.django_db
def test_letting_model(letting):
    expected_value = letting.title
    assert str(letting) == expected_value


def test_lettings_index_url():
    path = "/lettings/"
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings_index"


@pytest.mark.django_db
def test_letting_url(letting):
    path = f"/lettings/{letting.id}/"
    assert path == f"/lettings/{letting.id}/"
    assert resolve(path).view_name == "letting"


@pytest.mark.django_db
def test_lettings_index_view(client, letting):
    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200
    assert "lettings_list" in response.context
    assert len(response.context["lettings_list"]) == 1
    assert response.context["lettings_list"][0] == letting


@pytest.mark.django_db
def test_letting_view(client, letting):
    response = client.get(reverse("letting", kwargs={"letting_id": letting.id}))
    assert response.status_code == 200
    assert response.context["title"] == letting.title
    assert response.context["address"] == letting.address
