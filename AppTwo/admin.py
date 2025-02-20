from django.contrib import admin
from .models import Author, Detail

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
  list_display = ("name", "books", "date_of_birth",)

admin.site.register(Author)
admin.site.register(Detail)