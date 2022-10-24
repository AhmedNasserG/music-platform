from requests import Response
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer
from .models import User


class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        user_id = self.kwargs['pk']
        return get_object_or_404(User, pk=user_id)

    def put(self, request, *args, **kwargs):
        # TODO: fix this
        # user = self.get_object()
        # if user != request.user:
        #     return Response(status=403)
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # TODO: fix this
        # user = self.get_object()
        # if user != request.user:
        #     return Response(status=403)
        return self.partial_update(request, *args, **kwargs)
