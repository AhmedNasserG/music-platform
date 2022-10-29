from django.urls import path

from . import views

app_name = 'albums'

urlpatterns = [
    path('', views.AlbumViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='index'),
    path('songs', views.SongViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='songs'),
]
