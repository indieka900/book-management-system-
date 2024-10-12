from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import BookSerializer
from crud_app.models import Book

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)