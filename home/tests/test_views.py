import pytest
from django.urls import reverse


@pytest.fixture
def get_homepage_response(client):
    url = reverse('home:home')
    response = client.get(url)
    return response


def test_homepage_status_code(client):
    response = client.get('/')

    assert response.status_code == 200


def test_homepage_status_code_by_reverse(get_homepage_response):
    url = reverse('home:home')
    response = get_homepage_response.get(url)

    assert get_homepage_response.status_code == 200


def test_homepage_template(get_homepage_response):
    url = reverse('home:home')
    response = get_homepage_response.get(url)

    assert 'home/home.html' in [t.name for t in get_homepage_response.templates]


def test_homepage_contains_correct_html(get_homepage_response):
    url = reverse('home:home')
    response = get_homepage_response.get(url)

    assert 'Welcome to bookstore' in get_homepage_response.content.decode('UTF-8')
