from django.urls import path
from .views import (PublisherListView, PublisherDetailView,
                    HomePageView, AuthorListView, AuthorDetailView,
                    BookListView, BookDetailView)

app_name = 'book_app'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('publishers/', PublisherListView.as_view(), name='publisher_list'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(),
         name='publisher_detail'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(),
         name='author_detail'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(),
         name='book_detail'),
]
