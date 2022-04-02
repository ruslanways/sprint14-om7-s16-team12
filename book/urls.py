from django.urls import path
from . import views
urlpatterns=[
    path('',views.main_page),
    path('book_list/',views.book_list,name="book_list"),
]