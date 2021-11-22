from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from books.models import Book
from books.serializers import BookSerializer

class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        querySet = Book.objects.all()
        review = get_object_or_404(querySet, pk=pk)
        serializer = BookSerializer(review)
        return Response(serializer.data)
