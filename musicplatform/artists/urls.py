from django.urls import path

from . import views

app_name = 'artists'

urlpatterns = [
    path('', views.ArtistIndexView.as_view(), name='index'),
    path('create/', views.ArtistFormView.as_view(), name='create'),
]
