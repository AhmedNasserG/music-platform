from rest_framework.test import APITestCase, force_authenticate

from django.urls import reverse
from rest_framework import status
import factory

from albums.factories import AlbumFactory
from albums.models import Album
from artists.factories import ArtistFactory
from users.factories import UserFactory
from users.models import User


class AlbumTests(APITestCase):
    data = factory.build(dict, FACTORY_CLASS=AlbumFactory)
    url = reverse('albums:index')

    def test_unauthorized_create_album(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unvalid_create_album(self):
        user = UserFactory()
        self.client.force_authenticate(user=user)

        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_album(self):
        artist = ArtistFactory()
        self.data["artist"] = artist.id

        user = User.objects.get(pk=artist.user.id)
        self.client.force_authenticate(user=user)

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Album.objects.count(), 1)
        self.assertEqual(response.data['name'], self.data['name'])
        self.assertEqual(response.data['artist'], self.data['artist'])
        self.assertEqual(response.data['cost'], str(self.data['cost']))
        self.assertEqual(response.data['reviewed_by_admin'],
                         self.data['reviewed_by_admin'])

    def test_get_album(self):
        album = AlbumFactory()
        response = self.client.get(self.url, format='json')

        count = response.data['count']
        response_data = response.data['results'][0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(count, 1)
        self.assertEqual(response_data['name'], album.name)
        self.assertEqual(response_data['artist'], album.artist.id)
        self.assertEqual(response_data['cost'], str(album.cost))
        self.assertEqual(response_data['reviewed_by_admin'],
                         album.reviewed_by_admin)
