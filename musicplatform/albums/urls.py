from django.urls import path

from . import views

app_name = 'albums'

urlpatterns = [
    path('', views.AlbumIndexView.as_view(), name='index'),
    path('create/', views.AlbumFormView.as_view(), name='create'),
]
