from django.shortcuts import HttpResponseRedirect, render

from .forms import ArtistForm


def index(request):
    return render(request, 'artists/index.html')


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
