from django.db import models
from django.core.validators import FileExtensionValidator
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField

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


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True, default=album.name)
    image = models.ImageField(upload_to='songs/images/')
    thumbnail = ImageSpecField(
        source='image',
        format='JPEG',
    )
    audio = models.FileField(
        upload_to='songs/audio/',
        validators=[FileExtensionValidator(['mp3', 'wav'])]
    )
