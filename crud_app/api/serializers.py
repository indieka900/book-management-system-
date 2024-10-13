from rest_framework import serializers
from crud_app.models import Book

class BookSerializer(serializers.ModelSerializer):
    publishYear = serializers.CharField(source = 'year_published')
    author = serializers.CharField(source = 'auther')
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publishYear', 'createdAt', 'updatedAt']
        # read_only_fields = ['publishYear', 'author']