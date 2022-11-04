from rest_framework.test import APITestCase

from albums.models import Album
from albums.serializers import AlbumSerializer
from artists.factories import ArtistFactory


class AlbumSerializerTest(APITestCase):

    def test_serialize(self):
        artist = ArtistFactory()
        album = Album.objects.create(
            name='test',
            artist_id=artist.id,
            release_datetime='2023-05-15T08:15:12Z',
            cost=1.0,
            reviewed_by_admin=True,
        )
        serializer = AlbumSerializer(album)
        self.assertEqual(serializer.data, {
            'id': 1,
            'name': 'test',
            'artist': artist.id,
            'release_datetime': '2023-05-15T08:15:12Z',
            'created': serializer.data['created'],
            'modified': serializer.data['modified'],
            'cost': '1.00',
            'reviewed_by_admin': True,
        })

    def test_deserialize(self):
        artist = ArtistFactory()
        data = {
            'name': 'test',
            'artist': artist.id,
            'release_datetime': '2023-05-15T08:15:12Z',
            'cost': 1.0,
            'reviewed_by_admin': True,
        }
        serializer = AlbumSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Album.objects.count(), 1)
        self.assertEqual(Album.objects.get().name, 'test')
