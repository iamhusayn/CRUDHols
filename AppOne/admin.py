from django.contrib import admin
from .models import Book, Detail

# Register your models here.
class BookAdmin(admin.ModelAdmin):
  list_display = ("Tittle", "Author", "Status")
  search_fields = ('Tittle', 'Author', 'Field', 'Status', 'Published', 'Rating')

admin.site.register(Book)
admin.site.register(Detail)

