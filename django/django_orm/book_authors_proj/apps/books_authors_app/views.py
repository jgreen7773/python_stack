from django.shortcuts import render, redirect
from .models import Author, Book

def addbook(request):
    if request.method == "GET":
        data = Book.objects.all()
        context = {
            "book_list": data
        }
        return render(request, 'books_authors_app/addbook.html', context)
    if request.method == "POST":
        Book.objects.create(title=request.POST['Title'], desc=request.POST['Description'])
        return redirect('/')

def addauthor(request):
    if request.method == "GET":
        data = Author.objects.all()
        context = {
            "author_list": data
        }
        return render(request, 'books_authors_app/addauthor.html', context)
    if request.method == "POST":
        Author.objects.create(first_name=request.POST['Firstname'], last_name=request.POST['Lastname'])
        return redirect('/authors')

def displaybook(request, book_id):
    if request.method == "GET":
        data1 = Book.objects.get(id=book_id)
        data2 = Author.objects.all()
        data3 = Book.objects.get(id=book_id).Publishers
        context = {
            "this_book": data1,
            "all_authors": data2,
            "related_books": data3,
        }
        return render(request, 'books_authors_app/displaybook.html', context)
    if request.method == "POST":
        addbook = Book.objects.get(id=book_id)
        addbook.Publishers.add(request.POST['addauthortobook'])
        return redirect('/books/<id>')

def displayauthor(request, author_id):
    if request.method == "GET":
        data1 = Author.objects.get(id=author_id)
        data2 = Book.objects.all()
        data3 = Author.objects.get(id=author_id).books
        context = {
            "this_author": data1,
            "all_books": data2,
            "related_authors": data3,
        }
        return render(request, 'books_authors_app/displayauthor.html', context)
    if request.method == "POST":
        addauthor = Author.objects.get(id=author_id)
        addauthor.books.add(request.POST['addbooktoauthor'])
        return redirect('/authors/<id>')
