import factory
from factory.django import DjangoModelFactory

from .models import Artist


class ArtistFactory(DjangoModelFactory):
    class Meta:
        model = Artist

    stage_name = factory.Faker('name')
    social_media_link = factory.Faker('url')
    user = factory.SubFactory('users.factories.UserFactory')
