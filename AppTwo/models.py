from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    books = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    Published = models.DateField

    def __str__(self):
        return self.name
    
class Detail(models.Model):
    number_of_books = models.IntegerField

    def __str__(self):
        return self.number_of_books