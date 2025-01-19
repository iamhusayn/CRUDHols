from django.shortcuts import render #redirect
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from django.template import loader
from .models import Book
from .serializers import BookSerializer

# CRUD operations for different models. Examples:
# : Manage data related to "Books" (fields: title, author, publication_date, etc.).
# Create your views here.

class BookView(APIView):
    def view_books(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"message": "Welcome to your view. What books would you like to add?", "data": serializer.data})


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
