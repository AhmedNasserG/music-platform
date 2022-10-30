from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from artists.models import Artist
from .models import Album, Song
from .serializers import AlbumSerializer, SongSerializer


class IsArtistOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return Artist.objects.filter(user=request.user).exists()


class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.filter(reviewed_by_admin=True)
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtistOrReadOnly]

    def create(self, request, *args, **kwargs):
        request.data['artist'] = request.user.artist.id
        return super().create(request, *args, **kwargs)


class SongViewSet(ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
