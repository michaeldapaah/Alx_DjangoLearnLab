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


# HTTPS & Security Configuration

## Django Security Settings
- `SECURE_SSL_REDIRECT = True`: Redirects all HTTP traffic to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Forces browsers to use HTTPS for one year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to all subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows site to be submitted to the browser preload list.
- `SESSION_COOKIE_SECURE = True` and `CSRF_COOKIE_SECURE = True`: Ensure cookies are only transmitted via HTTPS.
- `X_FRAME_OPTIONS = "DENY"`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables XSS protection.

## Deployment
- HTTPS enabled with Let’s Encrypt SSL certificates.
- Nginx redirects all HTTP traffic to HTTPS.
