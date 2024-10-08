from django.shortcuts import get_object_or_404, render, redirect
from crud_app.models import Book

def home(request):
    books =Book.objects.all()
    context = {
        "books" : books,
    }
    
    return render(request, 'home.html', context)

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        auther = request.POST.get('auther')
        year_published = request.POST.get('year_published')
        Book.objects.create(
            title=title,
            auther = auther,
            year_published =year_published
        )
        return redirect('/')  
    return render(request,"add_book.html")
def update_book(request, id):
    book = get_object_or_404(Book, pk=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        auther = request.POST.get('auther') 
        year_published = request.POST.get('year_published')
        
        book.title = title
        book.auther = auther
        book.year_published = year_published
        book.save()
        
        return redirect('/')
    
    return render(request, "update_book.html", {'book': book})


def delete_book(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('/')

