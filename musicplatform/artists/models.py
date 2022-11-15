from django.db import models
from django.db.models import Count, Q

from users.models import User


class ArtistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(approved_albums=Count('album', filter=Q(album__reviewed_by_admin=True)))


class Artist(models.Model):
    stage_name = models.CharField(max_length=150, unique=True)
    social_media_link = models.URLField(max_length=250, blank=True, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = ArtistManager()

    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name
