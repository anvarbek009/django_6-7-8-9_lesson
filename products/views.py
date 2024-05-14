from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Book,Review
from .forms import AddReviewForm
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
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        reviews = Review.objects.filter(book=pk)
        print(reviews)
        context = {
            'book': book,
            'reviews': reviews
        }
        return render(request, 'book/book_detail.html', context=context)


class BookCreateView(CreateView):
    model = Book
    template_name = 'book/book_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products:book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/book_detail.html'
    success_url = reverse_lazy('products:book_list')

class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        books = Book.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'books': books,
            'add_review_form': add_review_form
        }
        return render(request, 'book/add_review.html', context=context)

    def post(self, request, pk):
        books = Book.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                book=books,
                user=request.user,
                rating=add_review_form.cleaned_data['rating']
            )

            review.save()
            return redirect('products:book_detail', pk=pk)
