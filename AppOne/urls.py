from django.contrib import admin
from django.urls import path #include
from . import views
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet

# router = DefaultRouter()
# router.register(r'Books', BookViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('home/', views.home, name='home'),
  path('cart/', views.cart),
  # path('books/', views.view_books(), ),
  # path('save/', views.save_user),
  # path('appone/', BookViewSet.as_view()),
]