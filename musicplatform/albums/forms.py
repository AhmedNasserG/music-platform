from django import forms
from django.forms import ModelForm

from .models import Album


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

    release_datetime = forms.DateField(widget=forms.SelectDateWidget())
