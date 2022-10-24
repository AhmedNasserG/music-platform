from django.shortcuts import HttpResponseRedirect, render
from django.views import View

from .forms import ArtistForm
from .models import Artist
from accounts.views import LoginRequieredView


class ArtistIndexView(View):
    tempalate_name = 'artists/index.html'

    def get(self, request):
        data = Artist.preview_all()
        return render(request, self.tempalate_name, {'data': data})


class ArtistFormView(LoginRequieredView):
    form_class = ArtistForm
    template_name = 'artists/create.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/artists/')
        return render(request, self.template_name, {'form': form})
