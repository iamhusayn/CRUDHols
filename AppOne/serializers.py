from rest_framework import serializers
from .models import Book, Detail

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Detail
    fields = '__all__'