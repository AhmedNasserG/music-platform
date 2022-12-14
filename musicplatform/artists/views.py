from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Artist
from .serializers import ArtistSerializer


class ArtistViewSet(ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)
