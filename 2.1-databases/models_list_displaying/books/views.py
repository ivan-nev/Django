from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Book
from django.urls import reverse
from django.core.paginator import Paginator

def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {'books':books}
    return render(request, template, context)

def book_view(request, pub_date):
    template = 'books/pub_date.html'

    books_object = get_list_or_404(Book, pub_date=pub_date)

    try:
        previous_object = (books_object[0]).get_previous_by_pub_date()
    except:
        previous_object = None
    try:
        next_object = (books_object[-1]).get_next_by_pub_date()
    except:
        next_object = None

    context = {'books':books_object, 'next':next_object, 'back':previous_object}
    print (context)
    return render(request, template, context)
