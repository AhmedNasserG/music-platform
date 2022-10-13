from django.urls import path

from . import views

app_name = 'artists'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]
