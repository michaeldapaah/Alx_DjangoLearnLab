from django.urls import path
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView
from . import views

urlpatterns = [
    path("books/", list_books, name="list_books"),   # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
    # Register view
    path("register/", views.register, name="register"),

    # Login view
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),

    # Logout view
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
]
