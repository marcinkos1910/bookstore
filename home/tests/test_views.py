import pytest
from django.urls import reverse


def test_homepage_status_code(client):
    response = client.get('/')

    assert response.status_code == 200


def test_homepage_status_code_by_reverse(client):
    url = reverse('home:home')
    response = client.get(url)

    assert response.status_code == 200


def test_homepage_template(client):
    url = reverse('home:home')
    response = client.get(url)

    assert 'home/home.html' in [t.name for t in response.templates]
