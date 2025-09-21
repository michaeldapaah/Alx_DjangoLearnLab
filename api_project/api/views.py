from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
# Create your views here.


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookViewSet(viewsets.ModelViewSet):
    """A viewset that provides CRUD operations for the Book model."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer