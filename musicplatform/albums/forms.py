from django import forms
from django.forms import ModelForm
from django.forms.models import BaseInlineFormSet


from .models import Album, Song


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

    release_datetime = forms.DateField(widget=forms.SelectDateWidget())


class AtLeastOneRequiredInlineFormSet(BaseInlineFormSet):

    def clean(self):
        """Check that at least one service has been entered."""
        super(AtLeastOneRequiredInlineFormSet, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
                   for cleaned_data in self.cleaned_data):
            raise forms.ValidationError('At least one item required.')
