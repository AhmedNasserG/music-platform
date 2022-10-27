from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve',
                                                 'put': 'update',
                                                 'patch': 'partial_update'}), name='user-detail'),
]
