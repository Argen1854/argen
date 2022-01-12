from django.shortcuts import get_object_or_404, render
from . models import Book

# Create your views here.

def books(request):
    books = Book.objects.all()
    return render(request, "book/index.html", {"books": books})

def book(request, id):
    book = get_object_or_404(Book, id = id)
    return render(request, 'book/book.html', {'book': book})