import pytest
from django.contrib.auth import get_user_model


# db decorator
@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(
        username= 'test_user',
        email= 'test@user.com',
        password= 'test'
    )

    assert User.objects.count() == 1
    assert user.username == 'test_user'
    assert user.email == 'test@user.com'
    assert not user.is_superuser
    assert not user.is_staff
    assert user.is_active


@pytest.mark.django_db
def test_create_superuser():
    User = get_user_model()
    user = User.objects.create_superuser(
        username= 'test_user',
        email= 'test@user.com',
        password= 'test'
    )

    assert User.objects.filter(is_superuser=True).count() == 1
    assert user.username == 'test_user'
    assert user.email == 'test@user.com'
    assert user.is_staff
    assert user.is_active
