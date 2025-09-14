# LibraryProject

This is my first Django project setup for the ALX Django Learn Lab.  
It contains the base configuration and shows the default Django welcome page.

# Introduction to Django

This project contains exercises for learning the basics of Django.

---

## Task 1: Django Models
- Created a `Book` model in the `bookshelf` app with the following fields:
  - `title` (CharField, max_length=100)
  - `author` (CharField, max_length=50)
  - `publication_year` (IntegerField)
- Ran migrations to apply the model to the database.

---

## Task 2: Django Admin Integration
- Registered the `Book` model in **bookshelf/admin.py** with a custom admin configuration.
- Added the following features to the Django Admin:
  - **List display**: shows `title`, `author`, `publication_year`.
  - **Search functionality**: search by `title` or `author`.
  - **Filter**: filter books by `publication_year`.
- Created a superuser to access the Django Admin:
  ```bash
  python manage.py createsuperuser
