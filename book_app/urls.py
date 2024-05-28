from django.urls import path
from .views import (PublisherListView, PublisherDetailView,
                    HomePageView, AuthorListView, AuthorDetailView, AuthorDeleteView,
                    BookListView, BookDetailView, PublisherCreateView, AuthorUpdateView,
                    AuthorCreateView, BookCreateView, BookDeleteView, BookUpdateView,
                    PublisherDeleteView, PublisherUpdateView, search)

app_name = 'book_app'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('publishers/', PublisherListView.as_view(), name='publisher_list'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(),
         name='publisher_detail'),
    path('publishers/add/', PublisherCreateView.as_view(), name='publisher_add'),
    path('publishers/<int:pk>/delete/',
         PublisherDeleteView.as_view(), name='publisher_delete'),
    path('publishers/<int:pk>/edit/',
         PublisherUpdateView.as_view(), name='publisher_edit'),

    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(),
         name='author_detail'),
    path('authors/add/', AuthorCreateView.as_view(), name='author_add'),
    path('authors/<int:pk>/delete/',
         AuthorDeleteView.as_view(), name='author_delete'),
    path('authors/<int:pk>/edit/',
         AuthorUpdateView.as_view(), name='author_edit'),

    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(),
         name='book_detail'),
    path('books/add/', BookCreateView.as_view(), name='book_add'),
    path('books/<int:pk>/delete/',
         BookDeleteView.as_view(), name='book_delete'),
    path('books/<int:pk>/edit/',
         BookUpdateView.as_view(), name='book_edit'),
    path('search/', search, name='search'),

]
