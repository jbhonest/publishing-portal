from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .models import Publisher, Author, Book


class HomePageView(TemplateView):
    template_name = "book_app/home.html"


class PublisherListView(ListView):
    model = Publisher
    context_object_name = "publishers"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = "publishers"
        return context


class PublisherDetailView(DetailView):
    model = Publisher
    context_object_name = 'publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(publisher=self.object)
        return context


class PublisherCreateView(CreateView):
    model = Publisher
    fields = ['name', 'address', 'city',
              'state_province', 'country', 'website']
    success_url = reverse_lazy('book_app:publisher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Publisher'
        return context


class PublisherUpdateView(UpdateView):
    model = Publisher
    fields = ['name', 'address', 'city',
              'state_province', 'country', 'website']
    success_url = reverse_lazy('book_app:publisher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Publisher'
        return context


class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = reverse_lazy('book_app:publisher_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.book_set.exists():
            messages.error(
                request, "This publisher cannot be deleted because it is assigned to one or more books.")
            return redirect('book_app:publisher_list')
        return super().delete(request, *args, **kwargs)


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = "books"
        return context


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'authors', 'publisher', 'publication_date', 'cover']
    success_url = reverse_lazy('book_app:book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Book'
        return context


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'authors', 'publisher', 'publication_date', 'cover']
    success_url = reverse_lazy('book_app:book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Book'
        return context


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_app:book_list')


class AuthorListView(ListView):
    model = Author
    context_object_name = "authors"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = "authors"
        return context


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(authors=self.object)
        return context


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'email', 'headshot']
    success_url = reverse_lazy('book_app:author_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Author'
        return context


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'email', 'headshot']
    success_url = reverse_lazy('book_app:author_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Author'
        return context


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('book_app:author_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.book_set.exists():
            messages.error(
                request, "This author cannot be deleted because they are assigned to one or more books.")
            return redirect('book_app:author_list')
        return super().post(request, *args, **kwargs)
