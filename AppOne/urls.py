from django.contrib import admin
from django.urls import path
from . import views
from .views import BookView, BookDetail

# router = DefaultRouter()
# router.register(r'Books', BookViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('home/', views.home, name='home'),
  path('cart/', views.cart),
  # path('books/', views.BookView()),
  # path('save/', views.save_user),
  # path('appone/', BookView.as_view()),
  path('bookviews/', BookView.as_view()),
  path('book/<int:pk>/', BookDetail.as_view()),
]