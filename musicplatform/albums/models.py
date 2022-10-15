from django.db import models
from model_utils.models import TimeStampedModel
from typing import Dict

from artists.models import Artist


class Album(TimeStampedModel):
    name = models.CharField(max_length=150, blank=True, default='New Album')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    reviewed_by_admin = models.BooleanField(
        default=False, help_text='Approve the album if its name is not explicit')

    def __str__(self):
        return self.name

    def preview(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'artist': self.artist.stage_name,
            'release_datetime': self.release_datetime,
            'cost': self.cost,
            'reviewed_by_admin': self.reviewed_by_admin,
        }

    @classmethod
    def preview_all(cls) -> Dict:
        return [album.preview() for album in cls.objects.all()]
