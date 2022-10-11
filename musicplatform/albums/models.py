from django.db import models
from django.utils import timezone

from artists.models import Artist


class Album(models.Model):
    name = models.CharField(max_length=150, blank=True, default='New Album')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    reviewed_by_admin = models.BooleanField(
        default=False, help_text='Approve the album if its name is not explicit')

    def __str__(self):
        return self.name
