from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from book.models import Book
# Create your views here.
def main_page(request):
    return render(request,"Books/Main_book_page.html")
def book_list(request):
    content=[i for i in Book.objects.all()]
    final=([[i.id,i.name,i.description,[author for author in i.authors.all()]] for i in content])
    return render(request,"Books/book_list.html",{"content":content})
def book_by_id(request,id):
    content=Book.objects.get(id=id)
    return render(request,"Books/book_page.html",{"book":content})

