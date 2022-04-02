from django.urls import path
from . import views
urlpatterns=[
    path('',views.main_page),
    path('book_list/',views.book_list,name="book_list"),
    path('book_list/id_<int:id>/',views.book_by_id,name="book_page"),
]