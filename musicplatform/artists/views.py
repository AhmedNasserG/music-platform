from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Artist
from .serializers import ArtistSerializer


class ArtistList(APIView):
    def get(self, request):
        artists = Artist.preview_all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
