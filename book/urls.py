from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books, name="books"),
    path('books/<int:id>/', views.book, name="book")
]
