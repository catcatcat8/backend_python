from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        querySet = User.objects.all()
        review = get_object_or_404(querySet, pk=pk)
        serializer = UserSerializer(review)
        return Response(serializer.data)
