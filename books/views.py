# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

from .models import Books


def index(request):
    books = Books.objects.all()
    context = {'books': books}
    return render(request, 'books/index.html', context)


def create(request):
    book = Books(book_title=request.POST['book_title'], writer=request.POST['writer'],
                 synopsis=request.POST['synopsis'], publisher=request.POST['publisher'],
                 publish_date=request.POST['publish_date'])
    book.save()
    return redirect('/')


def add_book(request):
    # members = Member.objects.all()
    books = Books.objects.all()
    context = {'books': books}
    return render(request, 'books/add_book.html', {})


def edit(request, id):
    # members = Member.objects.get(id=id)
    books = get_object_or_404(Books, pk=id)
    context = {'books': books}
    return render(request, 'books/edit.html', context)


def update(request, id):
    # member = Member.objects.get(id=id)
    books = get_object_or_404(Books, pk=id)
    books.book_title = request.POST['book_title']
    books.writer = request.POST['writer']
    books.synopsis = request.POST['synopsis']
    books.publisher = request.POST['publisher']
    books.publish_date = request.POST['publish_date']
    books.save()
    return redirect('/books/')


def delete(request, id):
    # member = Member.objects.get(id=id)
    member = get_object_or_404(Books, pk=id)
    member.delete()
    return redirect('/books/')
