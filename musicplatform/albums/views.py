from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from artists.models import Artist
from .models import Album, Song
from .serializers import AlbumSerializer, SongSerializer
from .tasks import send_congratulation_email


class IsArtistOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return Artist.objects.filter(user=request.user).exists()


class AlbumFilter(filters.FilterSet):
    cost__gte = filters.NumberFilter(field_name='cost', lookup_expr='gte')
    cost__lte = filters.NumberFilter(field_name='cost', lookup_expr='lte')
    name = filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = Album
        fields = ['name']


class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.filter(reviewed_by_admin=True)
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtistOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AlbumFilter

    def create(self, request, *args, **kwargs):
        request.data['artist'] = request.user.artist.id
        send_congratulation_email.delay('album')
        return super().create(request, *args, **kwargs)

    # send congratulation email to artist when album is created
    # def perform_create(self, serializer):
    #     # serialized_album = serializer.save()
    #     send_congratulation_email.delay('album')
    #     return super().perform_create(serializer)


class SongViewSet(ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
