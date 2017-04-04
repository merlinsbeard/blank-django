from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
                    many=True,
                    queryset=Book.objects.all())

    class Meta:
        model = Author
        fields = ('name', 'slug', 'book',)
