from django.contrib import admin
from django.urls import path 
from . import views
# from rest_framework.routers import DefaultRouter
from .views import AuthorsView, AuthorsDetail

# router = DefaultRouter()
# router.register(r'Author', AuthorsViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('authors/', views.authors, name='authors'),
  path('myauthors/', views.list_of_authors),
  # path('authors/', views.AuthorsViewSet.as_view()),
  # path('data/', views.getData),
  # path('add/', views.addAuthor),
  # path('apptwo/', AuthorsView.as_view()),
  path('authorviews/', AuthorsView.as_view()),
  path('author/<int:pk>/', AuthorsDetail.as_view()),
]