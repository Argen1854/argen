from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    return render(request, "max/index.html", {"task": tasks})

def about(request):
    return render(request, "max/about.html")