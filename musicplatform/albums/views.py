from django.shortcuts import HttpResponseRedirect, render

from .forms import AlbumForm
from .models import Album


def index(request):
    data = Album.preview_all()
    return render(request, 'albums/index.html', {'data': data})


def create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/artists/')
    else:
        form = AlbumForm()
    return render(request, 'albums/create.html', {'form': form})
