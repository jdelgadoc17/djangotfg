"""from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Book
from .serializers import UserSerializer, BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Book
from .serializers import UserSerializer, BookSerializer

@api_view(['GET'])
def get_books(request):
    """Retrieve all books."""
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_users(request):
    """Retrieve all books."""
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['POST'])
def create_user(request):
    """Registers a new user."""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
