from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "date_of_birth", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)

admin.site.register(Book, BookAdmin)