from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Album
from .serializers import AlbumSerializer


class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
