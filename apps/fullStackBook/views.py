from django.shortcuts import render, redirect
from .models import Book

def index(request):
    content = {
        'books': Book.objects.all()
        }
    print content
    return render(request, "fullStackBook/index.html", content)

def create(request):
    if request.method == "POST":
        Book.objects.create(
        title=request.POST['title'], 
        author=request.POST['author'],
        category=request.POST['category']
        )
        
    return redirect('/')
