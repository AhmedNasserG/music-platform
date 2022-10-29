from django.urls import path

from . import views

app_name = 'artists'

urlpatterns = [
    path('', views.ArtistViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='index'),
]
