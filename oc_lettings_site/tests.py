import pytest
from django.test import RequestFactory
from django.urls import reverse, resolve
from django.test import Client
from oc_lettings_site.views import error_500_view


@pytest.fixture
def client():
    return Client()


def test_index_url():
    path = reverse("index")
    assert path == "/"
    assert resolve(path).view_name == "index"


def test_index_view(client):
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "index.html" in [t.name for t in response.templates]


def test_404_view(client):
    response = client.get("/nonexistent-url/")
    assert response.status_code == 404
    assert "404.html" in [t.name for t in response.templates]


def test_500_handler():
    factory = RequestFactory()
    request = factory.get("/any-url/")
    response = error_500_view(request)

    assert response.status_code == 500
    assert b"500" in response.content
