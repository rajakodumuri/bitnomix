from django.http import Http404, HttpResponse
from django.shortcuts import render

from store.models import Categories, Authors, Books

# Create your views here.
def books_list(request):
    books = Books.objects.all()
    bookList = {'books': books}
    return render(request, 'books.html', bookList)

def categories_list(request,pk):
    categories = Categories.objects.all()
    books = Books.objects.filter(category=pk)
    categoryList = {'categories': categories, 'books': books}
    return render(request, 'categories.html', categoryList)
