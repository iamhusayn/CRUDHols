from django.shortcuts import render #redirect
from rest_framework.views import APIView
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
from django.template import loader
from .models import Book, Detail
from .serializers import BookSerializer, DetailSerializer

# CRUD operations for different models. Examples:
# : Manage data related to "Books" (fields: title, author, publication_date, etc.).
# Create your views here.

class BookView(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        detail = self.request.query_params.get('detail')
        if detail is not None:
            queryset = queryset.filter(bookPages=detail)
        return queryset
        
        # return Response({"message": "Welcome to your view. What books would you like to add?", "data": serializer.data})

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


def home(request): 
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
# render (request, "index.html", context={})
#HttpResponse("Hello World")
    
def cart(request):
    mybooks = Book.objects.all().values()
    template = loader.get_template('all_books.html')
    context = {
        'mybooks': mybooks,
    }
    return HttpResponse(template.render(context, request))

def save_user(request):
    users_name = request.POST['users_name']
    return render(request,"welcome.html",context={'users_name':users_name})

# # Create your views here.
