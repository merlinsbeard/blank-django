from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author')

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
            many=True, view_name='book-detail', read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
