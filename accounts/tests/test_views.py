import pytest
from django.urls import reverse
from django.test import Client
from accounts.forms import CustomUserCreationForm


@pytest.fixture
def get_signup_response(db):
    client = Client(enforce_csrf_checks=True)
    url = reverse('account_signup')
    response = client.get(url)
    return response


def test_signup_status_code(client, db):
    response = client.get('/accounts/signup/')
    assert response.status_code == 200


def test_signup_reverse(get_signup_response):
    assert get_signup_response.status_code == 200
    assert 'account/signup.html' in [t.name for t in get_signup_response.templates]
    assert 'Sign Up' in get_signup_response.content.decode('UTF-8')
