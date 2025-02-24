"""from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'register', UserViewSet, basename='register')  # ✅ Now this will handle `/api/register/`

urlpatterns = [
    path('', include(router.urls)),  # ✅ Add all router-generated URLs
]
"""


from django.urls import path
from .views import create_user, get_books, get_all_users

urlpatterns = [
    path('register/', create_user, name='register'),
    path('books/', get_books, name='books'),
    path('users/', get_all_users, name='all_users'),
]
