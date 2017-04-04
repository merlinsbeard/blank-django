from django.test import TestCase
from .models import Book, Author


class BookTestCase(TestCase):
    def setUp(self):
        a = Author.objects.create(name="Author", slug="author")
        Book.objects.create(author=a, name="Wolds end", slug="worlds-ends")

    def test_book_exists(self):
        book = Book.objects.get(slug="worlds-ends")
        self.assertEqual(book.slug, 'worlds-ends')
