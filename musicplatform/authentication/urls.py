from django.urls import path

from . import views

app_name = 'authentication'

urlpatterns = [
    path('register', views.RegisterUserAPIView.as_view(), name='index'),
    path('login', views.LoginUserAPIView.as_view(), name='index'),
    path('logout', views.LogoutUserAPIView.as_view(), name='index'),
]
