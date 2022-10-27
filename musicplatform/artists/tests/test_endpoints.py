import factory
from rest_framework.test import APITestCase, force_authenticate
from django.core import serializers
from django.urls import reverse
from rest_framework import status

from artists.factories import ArtistFactory
from artists.models import Artist
from users.factories import UserFactory


class ArtistTests(APITestCase):
    data = factory.build(dict, FACTORY_CLASS=ArtistFactory)
    url = reverse('artists:index')

    def test_unauthorized_create_artist(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_artist(self):
        user = UserFactory()
        self.client.force_authenticate(user=user)

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 1)
        self.assertEqual(Artist.objects.get().stage_name,
                         self.data['stage_name'])

    def test_unvalid_create_artist(self):
        user = UserFactory()
        self.client.force_authenticate(user=user)

        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(
            self.url, {'social_media_link': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_artist(self):
        artist = ArtistFactory()
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['stage_name'], artist.stage_name)
        self.assertEqual(
            response.data[0]['social_media_link'], artist.social_media_link)
