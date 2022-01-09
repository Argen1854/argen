from django.shortcuts import render
from . models import Book

# Create your views here.

def book(request):
    book = Book.objects.all()
    return render(request, "book/index.html", {"book": book})