from django.urls import path 
from .views import ListView, BookListView,BookDetailView,BookCreateView,BookDeleteView


app_name = 'products'
urlpatterns = [
    path('books/',BookListView.as_view(),name='book_list'),
    path('deatail/<int:pk>',BookDetailView.as_view(),name='book_detail'),
    path('create/',BookCreateView.as_view(),name='book_create'),
    path('delete/<int:pk>',BookDeleteView.as_view(),name='book_delete'),

]