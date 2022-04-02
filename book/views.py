from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book
# Create your views here.
def main_page(request):
    return render(request,"Books/Main_book_page.html")
def book_list(request):
    content=list(Book.objects.all())
    return HttpResponse(content)

