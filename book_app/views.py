from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.template.loader import render_to_string
from .models import Publisher, Author, Book
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from weasyprint import HTML
from django.contrib.auth.mixins import LoginRequiredMixin


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
            queryset = queryset.filter(Q(name__icontains=query))
        return queryset


class PublisherDetailView(DetailView):
    model = Publisher
    context_object_name = 'publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(publisher=self.object)
        return context


class PublisherCreateView(LoginRequiredMixin, CreateView):
    model = Publisher
    fields = ['name', 'address', 'city',
              'state_province', 'country', 'website']
    success_url = reverse_lazy('book_app:publisher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Publisher'
        context['cancel_url'] = reverse('book_app:publisher_list')
        return context


class PublisherUpdateView(LoginRequiredMixin, UpdateView):
    model = Publisher
    fields = ['name', 'address', 'city',
              'state_province', 'country', 'website']

    def get_success_url(self):
        return reverse('book_app:publisher_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Publisher'
        context['cancel_url'] = reverse(
            'book_app:publisher_detail', kwargs={'pk': self.object.pk})
        return context


class PublisherDeleteView(LoginRequiredMixin, DeleteView):
    model = Publisher
    success_url = reverse_lazy('book_app:publisher_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.book_set.exists():
            messages.error(
                request, "This publisher cannot be deleted because it is assigned to one or more books.")
            return redirect('book_app:publisher_list')
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = reverse(
            'book_app:publisher_detail', kwargs={'pk': self.object.pk})
        return context


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
            queryset = queryset.filter(Q(name__icontains=query))
        return queryset


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(authors=self.object)
        return context


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name', 'email', 'headshot']
    success_url = reverse_lazy('book_app:author_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Author'
        context['cancel_url'] = reverse('book_app:author_list')
        return context


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['name', 'email', 'headshot']

    def get_success_url(self):
        return reverse('book_app:author_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Author'
        context['cancel_url'] = reverse(
            'book_app:author_detail', kwargs={'pk': self.object.pk})
        return context


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('book_app:author_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.book_set.exists():
            messages.error(
                request, "This author cannot be deleted because they are assigned to one or more books.")
            return redirect('book_app:author_list')
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = reverse(
            'book_app:author_detail', kwargs={'pk': self.object.pk})
        return context


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
            queryset = queryset.filter(Q(title__icontains=query))
        return queryset


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'authors', 'publisher', 'publication_date', 'cover']
    success_url = reverse_lazy('book_app:book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Book'
        context['cancel_url'] = reverse('book_app:book_list')
        return context


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'authors', 'publisher', 'publication_date', 'cover']

    def get_success_url(self):
        return reverse('book_app:book_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Book'
        context['cancel_url'] = reverse(
            'book_app:book_detail', kwargs={'pk': self.object.pk})
        return context


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book_app:book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = reverse(
            'book_app:book_detail', kwargs={'pk': self.object.pk})
        return context


def search(request):
    query = request.GET.get('query')
    authors = Author.objects.filter(
        Q(name__icontains=query))
    books = Book.objects.filter(Q(title__icontains=query))
    publishers = Publisher.objects.filter(Q(name__icontains=query))

    context = {
        'query': query,
        'authors': authors,
        'books': books,
        'publishers': publishers
    }
    return render(request, 'book_app/search_results.html', context)


def book_detail_pdf(request, pk):
    book = get_object_or_404(Book, pk=pk)
    html_string = render_to_string(
        'book_app/book_detail_pdf.html', {'book': book})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={book.title}.pdf'
    html.write_pdf(response)
    return response
