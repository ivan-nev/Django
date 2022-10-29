from django.shortcuts import render, get_object_or_404, redirect
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

    # count = 15
    # page_num = int(request.GET.get('page', 10))
    books = Book.objects.all().order_by('pub_date')
    paginator = Paginator(books,1)
    page1 = paginator.get_page(1)
    page2 = paginator.get_page(2)
    page3 = paginator.get_page(3)
    page4 = paginator.get_page(4)
    print(page4)

    # books_object = get_object_or_404(Book, pub_date=pub_date)
    # try:
    #     previous_object = books_object.get_previous_by_pub_date()
    # except:
    #     previous_object = None
    # try:
    #     next_object = books_object.get_next_by_pub_date()
    # except:
    #     next_object = None


    # data = page.object_list

    books = Book.objects.all().filter(pub_date=pub_date)
    # books = Book.objects.all().order_by('pub_date')
    context = {'books':books}
    print (context)
    return render(request, template, context)
