import os
import django

# Setup Django environment (so we can run this script directly)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from .models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return []

# 2. List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


if __name__ == "__main__":
    # Example usage
    print("Books by 'J.K. Rowling':", books_by_author("J.K. Rowling"))
    print("Books in 'Central Library':", books_in_library("Central Library"))
    print("Librarian of 'Central Library':", librarian_of_library("Central Library"))
