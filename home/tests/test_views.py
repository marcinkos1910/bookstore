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


@pytest.fixture
def get_about_page_response(client):
    url = reverse('home:about')
    response = client.get(url)
    return response


def test_about_page_status_code(client):
    response = client.get('/about/')
    assert response.status_code == 200


def test_about_page_status_code_by_reverse(get_about_page_response):
    assert get_about_page_response.status_code == 200


def test_about_page_template(get_about_page_response):
    assert 'home/about.html' in [t.name for t in get_about_page_response.templates]


def test_about_page_contains_correct_html(get_about_page_response):
    assert 'About' in get_about_page_response.content.decode('UTF-8')
