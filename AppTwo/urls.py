from django.contrib import admin
from django.urls import path 
from . import views
from .views import AuthorsView, AuthorsDetail

urlpatterns = [
  path('admin/', admin.site.urls),
  path('authors/', views.authors, name='authors'),
  path('myauthors/', views.list_of_authors),
  path('authorviews/', AuthorsView.as_view()),
  path('author/<int:pk>/', AuthorsDetail.as_view()),
]