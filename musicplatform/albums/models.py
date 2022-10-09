from django.db import models
from django.utils import timezone


class Album(models.Model):
    name = models.CharField(max_length=150, blank=True, default='New Album')
    artist = models.ForeignKey(
        'artists.Artist', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    release_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
