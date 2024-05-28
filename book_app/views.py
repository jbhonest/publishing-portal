from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .models import Publisher, Author, Book
from django.db.models import Q
from django.shortcuts import render


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

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(city__icontains=query) | Q(
                state_province__icontains=query) | Q(country__icontains=query))
        return queryset


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

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(
                authors__name__icontains=query) | Q(publisher__name__icontains=query)).distinct()
        return queryset


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

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(email__icontains=query))
        return queryset


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


def search(request):
    query = request.GET.get('query')
    authors = Author.objects.filter(
        Q(name__icontains=query) | Q(email__icontains=query))
    books = Book.objects.filter(Q(title__icontains=query) | Q(
        authors__name__icontains=query) | Q(publisher__name__icontains=query)).distinct()
    publishers = Publisher.objects.filter(Q(name__icontains=query) | Q(
        city__icontains=query) | Q(country__icontains=query))

    context = {
        'query': query,
        'authors': authors,
        'books': books,
        'publishers': publishers
    }
    return render(request, 'book_app/search_results.html', context)
