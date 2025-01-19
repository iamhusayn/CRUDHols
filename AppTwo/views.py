from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author, Detail
from .serializers import AuthorSerializer, DetailSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

# CRUD operations for different models. Examples:
# : Manage data related to "Authors" (fields: name, bio, date_of_birth, etc.).
# Create your views here. 
# class AuthorsViewSet(APIView):
class AuthorsView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


def authors(request):
    template = loader.get_template('apptwo.html')
    return HttpResponse(template.render())

def list_of_authors(request):
    myauthors = Author.objects.all().values()
    template = loader.get_template('all_authors.html')
    context = {
        'myauthors': myauthors,
    }
    return HttpResponse(template.render(context, request))