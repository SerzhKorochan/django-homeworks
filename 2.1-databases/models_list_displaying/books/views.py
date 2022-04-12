import imp
from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }

    return render(request, template, context)


def pub_date_view(request, pub_date):
    template = 'books/books_list.html'
    books_objects = Book.objects.all()
    books = books_objects.filter(pub_date=pub_date)

    previous_book_objects = books_objects.filter(pub_date__lt=pub_date)
    next_book_objects = books_objects.filter(pub_date__gt=pub_date)
    previous_pub_date = False
    next_pub_date = False
    date_format = "%Y-%m-%d"
    
    if previous_book_objects.count() > 0:
        previous_pub_date = previous_book_objects[0].pub_date.strftime(date_format)
    
    if next_book_objects.count() > 0:
        next_pub_date = next_book_objects[0].pub_date.strftime(date_format)

    context = {
        'books': books,
        'previous_pub_date': previous_pub_date,
        'next_pub_date': next_pub_date
    }

    return render(request, template, context)
