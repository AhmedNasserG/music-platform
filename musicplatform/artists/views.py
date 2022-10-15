from django.shortcuts import HttpResponseRedirect, render

from .forms import ArtistForm
from .models import Artist


def index(request):
    data = Artist.preview_all()
    return render(request, 'artists/index.html', {'data': data})


def create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/artists/')
    else:
        form = ArtistForm()
    return render(request, 'artists/create.html', {'form': form})
