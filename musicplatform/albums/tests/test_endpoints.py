from rest_framework.test import APITestCase, force_authenticate

from django.urls import reverse
from rest_framework import status
import factory

from albums.factories import AlbumFactory
from albums.models import Album
from artists.factories import ArtistFactory
from artists.models import Artist
from users.factories import UserFactory


class AlbumTests(APITestCase):
    # TODO: refactor creating the data
    data = factory.build(dict, FACTORY_CLASS=AlbumFactory)
    url = reverse('albums:index')

    def test_unauthorized_create_album(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unvalid_create_album(self):
        user = UserFactory()
        self.client.force_authenticate(user=user)

        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_album(self):
        artist = ArtistFactory()
        self.data["artist"] = artist.id

        user = UserFactory()
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

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], album.name)
        self.assertEqual(response.data[0]['artist'], album.artist.id)
        self.assertEqual(response.data[0]['cost'], str(album.cost))
        self.assertEqual(response.data[0]['reviewed_by_admin'],
                         album.reviewed_by_admin)
