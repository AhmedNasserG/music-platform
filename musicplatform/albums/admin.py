from django.contrib import admin

from .forms import AtLeastOneRequiredInlineFormSet
from .models import Album, Song


class SongInline(admin.TabularInline):
    model = Song
    formset = AtLeastOneRequiredInlineFormSet


class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInline, ]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)
