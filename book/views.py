from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from book.models import Book
from order.models import Order
from author.models import Author
# Create your views here.
def main_page(request):
    return render(request,"Books/Main_book_page.html")
def book_list(request):
    content=[i for i in Book.objects.all()]
    final=([[i.id,i.name,i.description,[author for author in i.authors.all()]] for i in content])
    return render(request,"Books/book_list.html",{"content":content})
def book_by_id(request,id):
    try:
        content=Book.objects.get(id=id)
        return render(request,"Books/book_page.html",{"book":content})
    except:
        return HttpResponseNotFound("NOT FOUND 404")
def unordered_books(request):
    orders=[i.book for i in Order.objects.all()]
    books=list(Book.objects.all())
    content=[]
    for i in books:
        if i not in orders:
            content.append(i)
    return render(request,"Books/unordered_book.html",{"content":content})
def book_by_author(request,author):
    try:
        content=Author.objects.get(name=author).books.all()
        return render(request,"Books/book_list.html",{"content":content})
    except:
        return HttpResponseNotFound("NOT FOUND 404")
def book_by_user(request,id):
    content=[]
    try:
        for order in Order.objects.all():
            print(order.user)
            if order.user.id==id:
                content.append(order.book)
        return render(request,"Books/book_list.html",{"content": content})
    except:
        return HttpResponseNotFound("NOT FOUND 404")
def book_by_author_id(request,id):
    try:
        content=Author.objects.get(pk=id).books.all()
        return render(request,"Books/book_list.html",{"content":content})
    except:
        return HttpResponseNotFound("NOT FOUND 404")
def sort_name_asc(request):
    content=sorted(list(Book.objects.all()),key=lambda i:i.name)
    return render(request, "Books/book_list.html", {"content": content})
def sort_name_desc(request):
    content=sorted(list(Book.objects.all()),key=lambda i:i.name)[::-1]
    return render(request, "Books/book_list.html", {"content": content})
def sort_count_asc(request):
    content = sorted(list(Book.objects.all()), key=lambda i: i.count)
    return render(request, "Books/book_list.html", {"content": content})
def sort_count_desc(request):
    content = sorted(list(Book.objects.all()), key=lambda i: i.count)[::-1]
    return render(request, "Books/book_list.html", {"content": content})




