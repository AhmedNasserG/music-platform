from django.db import models


class Artist(models.Model):
    stage_name = models.CharField(
        max_length=150)
    social_media_link = models.URLField(max_length=250, blank=True, default='')

    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name
