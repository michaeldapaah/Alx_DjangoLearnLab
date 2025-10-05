"""
Models for the Advanced API Project.
Defines Author and Book models with a one-to-many relationship.
Each Author can have multiple Books.
"""
"""
This module defines Django REST Framework serializers for the advanced API project.
It demonstrates nested serialization where Author includes a list of its Books.
"""

from django.db import models
from django.utils import timezone

class Author(models.Model):
    """Represents an author who can have multiple books."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Represents a book written by an author."""
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
