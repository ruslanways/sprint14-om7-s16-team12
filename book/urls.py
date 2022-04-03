from django.urls import path
from . import views
urlpatterns=[
    path('',views.main_page),
    path('book_list/',views.book_list,name="book_list"),
    path('book_list/id_<int:id>/',views.book_by_id,name="book_page"),
    path('unordered_books/',views.unordered_books,name="unordered_books"),
    path('book_list/author_<author>/',views.book_by_author),
    path('book_list/authorid_<int:id>/', views.book_by_author_id),
    path('book_list/user_<int:id>/',views.book_by_user),
    path('book_list/sorted_name_asc/',views.sort_name_asc),
    path('book_list/sorted_name_desc/', views.sort_name_desc),
    path('book_list/sorted_count_asc/',views.sort_count_asc),
    path('book_list/sorted_count_desc/', views.sort_count_desc),
]