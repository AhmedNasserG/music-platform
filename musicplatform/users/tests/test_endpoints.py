from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status
from django.urls import reverse

from users.factories import UserFactory


class UsersTest(APITestCase):
    url = reverse('users:user-list')

    def test_unauthorized_list_users(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_users(self):
        user = UserFactory()

        self.client.force_authenticate(user=user)

        response = self.client.get(self.url, format='json')
        count = response.data['count']
        response_data = response.data['results'][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(count, 1)
        self.assertEqual(response_data['username'], user.username)
        self.assertEqual(response_data['email'], user.email)
        self.assertEqual(response_data['bio'], user.bio)

    def test_get_user(self):
        user = UserFactory()

        self.client.force_authenticate(user=user)

        response = self.client.get(self.url + f'{user.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user.username)

    def test_unauthorized_edit_user(self):
        requset_user = UserFactory()
        testing_user = UserFactory()

        self.client.force_authenticate(user=requset_user)

        response = self.client.patch(
            self.url + f'{testing_user.id}/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_edit_user(self):
        requset_user = UserFactory()

        self.client.force_authenticate(user=requset_user)

        response = self.client.patch(
            self.url + f'{requset_user.id}/', {'bio': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bio'], 'test')
