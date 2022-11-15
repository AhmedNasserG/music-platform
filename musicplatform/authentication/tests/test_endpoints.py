from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status
from django.urls import reverse


from users.factories import UserFactory
from users.models import User


class AuthenticationTest(APITestCase):
    register_url = reverse('authentication:register')
    login_url = reverse('authentication:login')
    logout_url = reverse('authentication:logout')

    def test_bad_register(self):
        data = {
            'username': 'test_username',
            'email': 'test_email@test.com',
            'password1': 'test_password',
            'password2': 'test_password_diff',
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register(self):
        data = {
            'username': 'test_username',
            'email': 'test_email@test.com',
            'password1': 'test_password',
            'password2': 'test_password',
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_login(self):
        user = UserFactory()

        data = {
            'username': user.username,
            'password': 'wrong_password',
        }

        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


def test_unauthorized_logout(self):
    response = self.client.post(self.logout_url, format='json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


def test_logout(self):
    user = UserFactory()

    self.client.force_authenticate(user=user)

    response = self.client.post(self.logout_url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
