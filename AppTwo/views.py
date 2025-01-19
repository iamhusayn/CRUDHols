from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from .serializer import AuthorSerializer
# from .models import Author

# CRUD operations for different models. Examples:
# : Manage data related to "Authors" (fields: name, bio, date_of_birth, etc.).
# Create your views here. 
# class AuthorsViewSet(APIView):
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

    #   author = Author.objects.all()
    #   serializer = AuthorSerializer(author, many=True)
    # return HttpResponse("Welcome to the author's page.") 
    

# @api_view(['GET'])
# def getData(request):
#   items = Author.objects.all()
#   serializer = AuthorSerializer(items, many=True)
#   return Response(serializer.data)

# @api_view(['POST'])
# def addAuthor(request):
#   serializer = AuthorSerializer(data=request.data)
#   if serializer.is_valid():
#     serializer.save()
#   return Response()