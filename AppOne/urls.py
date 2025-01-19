from django.contrib import admin
from django.urls import path
from . import views
from .views import BookView, BookDetail


urlpatterns = [
  path('admin/', admin.site.urls),
  path('home/', views.home, name='home'),
  path('cart/', views.cart),
  path('bookviews/', BookView.as_view()),
  path('book/<int:pk>/', BookDetail.as_view()),
]