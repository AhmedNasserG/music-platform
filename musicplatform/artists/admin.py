from django.contrib import admin

from .models import Artist
from albums.models import Album


class AlbumInline(admin.TabularInline):
    model = Album


class ArtistAdmin(admin.ModelAdmin):
    inlines = [
        AlbumInline,
    ]


admin.site.register(Artist, ArtistAdmin)
