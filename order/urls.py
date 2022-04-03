from django.urls import path
from . import views
urlpatterns=[
    path('list_sorted_created_asc/',views.sorted_created_asc),
    path('list_sorted_created_desc/',views.sorted_created_desc),
    path('list_sorted_plated_asc/', views.sorted_plated_asc),
    path('list_sorted_plated_desc/', views.sorted_plated_desc),
    path('not_in_time/',views.not_in_time),
]