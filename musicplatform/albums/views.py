from django.shortcuts import HttpResponseRedirect, render
from django.views import View

from .forms import AlbumForm
from .models import Album
from accounts.views import LoginRequieredView


class AlbumIndexView(View):
    tempalate_name = 'albums/index.html'

    def get(self, request):
        data = Album.preview_all()
        return render(request, self.tempalate_name, {'data': data})


class AlbumFormView(LoginRequieredView):
    form_class = AlbumForm
    template_name = 'albums/create.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/artists/')
        return render(request, self.template_name, {'form': form})
