from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Album, Song
from .serializers import AlbumSerializer, SongSerializer


class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.filter(reviewed_by_admin=True)
    permission_classes = [IsAuthenticatedOrReadOnly]


class SongViewSet(ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
