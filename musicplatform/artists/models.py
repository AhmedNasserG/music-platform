from django.db import models
from django.db.models import Count, Q
from typing import Dict


class ArtistManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(approved_albums=Count('album', filter=Q(album__reviewed_by_admin=True)))


class Artist(models.Model):
    stage_name = models.CharField(max_length=150, unique=True)
    social_media_link = models.URLField(max_length=250, blank=True, default='')

    objects = ArtistManager()

    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name

    def preview(self) -> Dict:
        return {
            'id': self.id,
            'stage_name': self.stage_name,
            'social_media_link': self.social_media_link,
            'approved_albums': self.approved_albums,
            'albums': [album.preview() for album in self.album_set.all()],
        }

    @classmethod
    def preview_all(cls) -> Dict:
        return [artist.preview() for artist in cls.objects.all()]
