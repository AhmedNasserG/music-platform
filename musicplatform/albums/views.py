from django.shortcuts import HttpResponseRedirect, render

from .forms import AlbumForm


def index(request):
    return render(request, 'albums/index.html')


def create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/artists/')
    else:
        form = AlbumForm()
    return render(request, 'albums/create.html', {'form': form})
