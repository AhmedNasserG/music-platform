import factory
from factory.django import DjangoModelFactory
from django.utils import timezone

from .models import Album, Song


class AlbumFactory(DjangoModelFactory):
    class Meta:
        model = Album

    name = factory.Faker('name')
    artist = factory.SubFactory('artists.factories.ArtistFactory')
    release_datetime = factory.Faker(
        'date_time', tzinfo=timezone.get_current_timezone())
    cost = factory.Faker('pydecimal', left_digits=2,
                         right_digits=2, positive=True)
    reviewed_by_admin = True


class SongFactory(DjangoModelFactory):
    class Meta:
        model = Song

    album = factory.SubFactory(AlbumFactory)
    name = factory.Faker('name')
    image = factory.django.ImageField()
    audio = factory.django.FileField(filename='test.mp3')
