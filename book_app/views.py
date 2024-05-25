from django.views.generic import ListView, DetailView, TemplateView
from .models import Publisher, Author, Book


class HomePageView(TemplateView):
    template_name = "book_app/home.html"


class PublisherListView(ListView):
    model = Publisher
    context_object_name = "publishers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = "publishers"
        return context


class AuthorListView(ListView):
    model = Author
    context_object_name = "authors"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = "authors"
        return context


class BookListView(ListView):
    model = Book
    context_object_name = "books"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbar'] = "books"
        return context


class PublisherDetailView(DetailView):
    model = Publisher
    context_object_name = 'publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(publisher=self.object)
        return context


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(authors=self.object)
        return context


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
