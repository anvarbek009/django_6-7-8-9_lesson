from django.views.generic import ListView, DetailView, UpdateView,CreateView,   DeleteView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Book
from django.urls import reverse_lazy
# Create your views here.

# class ListView(View):
#     def get(self,request):
#         book=Book.objects.all().order_by('-pk')
#         return render(request, 'book/book_list.html',{'book':book})

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'book'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'


class BookCreateView(CreateView):
    model = Book
    template_name = 'book/book_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products:book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/book_detail.html'
    success_url = reverse_lazy('products:book_list')
