from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Author, Detail

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Detail
    fields = '__all__'