from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from knox.models import AuthToken
from rest_framework.response import Response

from users.serializers import UserSerializer

from .serializers import RegisterSerializer, LoginSerializer


class RegisterUserAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
            "token": token[1],
            "users": UserSerializer(user, context=self.get_serializer_context()).data,
        })


class LoginUserAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "token": AuthToken.objects.create(user)[1],
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })
