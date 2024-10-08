from django.shortcuts import get_object_or_404, render, redirect
from crud_app.forms import BookForm
from crud_app.models import Book

def generate_dummy_books():
    dummy_books = [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year_published": 1960},
        {"title": "1984", "author": "George Orwell", "year_published": 1949},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year_published": 1925},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "year_published": 1813},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year_published": 1951},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year_published": 1937},
        {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "year_published": 1997},
        {"title": "The Hunger Games", "author": "Suzanne Collins", "year_published": 2008},
        {"title": "The Da Vinci Code", "author": "Dan Brown", "year_published": 2003},
        {"title": "The Alchemist", "author": "Paulo Coelho", "year_published": 1988},
        {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "year_published": 2005},
        {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "year_published": 1979},
    ]

    for book_data in dummy_books:
        book = Book(
            title=book_data['title'],
            auther=book_data['author'],  # Note: 'auther' is misspelled as in your original code
            year_published=book_data['year_published'],
            # date_created=timezone.now()
        )
        book.save()
        print(f"Created book: {book.title}")

    print(f"Created {len(dummy_books)} dummy books.")

def home(request):
    books =Book.objects.all()
    context = {
        "books" : books,
    }
    
    return render(request, 'home.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()
    return render(request, "book.html", {'form': form})

def update_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(instance=book)
    return render(request, "book.html", {'form': form})


def delete_book(request, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return redirect('/')

