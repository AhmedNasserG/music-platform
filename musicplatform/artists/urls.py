from django.urls import path

from . import views

app_name = 'artists'

urlpatterns = [
    path('', views.ArtistList.as_view(), name='index'),
]
