from django.shortcuts import render
from order.models import Order
# Create your views here.
def sorted_created_asc(request):
    content=sorted(list(Order.objects.all()),key=lambda x: x.created_at)[::-1]
    return render(request,"Orders/list_of_orders.html",{"content": content})
def sorted_created_desc(request):
    content = sorted(list(Order.objects.all()), key=lambda x: x.created_at)
    return render(request, "Orders/list_of_orders.html", {"content": content})
def sorted_plated_asc(request):
    content=sorted(list(Order.objects.all()),key=lambda x: x.plated_end_at)[::-1]
    return render(request,"Orders/list_of_orders.html",{"content": content})
def sorted_plated_desc(request):
    content=sorted(list(Order.objects.all()),key=lambda x: x.plated_end_at)
    return render(request,"Orders/list_of_orders.html",{"content": content})
def not_in_time(request):
    content=[]
    for order in Order.objects.all():
        if order.end_at==None:
            content.append(order.user)
    return render(request,"User/user_list.html",{"content":content})

