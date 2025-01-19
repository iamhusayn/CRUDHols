from django.shortcuts import render #redirect
# from rest_framework.views import APIView
from django.http import HttpResponse
from django.template import loader
from .models import Book
# from .serializer import BooksSerializer

# CRUD operations for different models. Examples:
# : Manage data related to "Books" (fields: title, author, publication_date, etc.).
# Create your views here.

# class BookViewSet(APIView):
# def view_books(self, request):
        # books = AddBooks.objects.all()
        # serializer = BooksSerializer(books, many=True)
    #return HttpResponse("Welcome to your cart. What books will you like to add?")

def home(request): 
    template = loader.get_template('appone.html')
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

# def save_user(request):
#     users_name = request.POST['users_name']
#     return render(request,"welcome.html",context={'users_name':users_name})

# # Create your views here.
