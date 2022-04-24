from django.urls import path

from books.views import get_uuids_a, get_uuids_b, get_argument_from_path, get_argument_from_query, \
    check_http_query_type, get_headers, raise_error_for_fun, AuthorListBasedView, CategoryListTemplateView, \
    BookListView, BookDetailsView, CategoryCreateFormView, AuthorCreateView, AuthorUpdateView, BookCreateView, \
    BookUpdateView

urlpatterns = [
    path('uuids-a', get_uuids_a),
    path('uuids-b', get_uuids_b),
    path('path-args/<int:x>/<str:y>/<slug:z>/', get_argument_from_path, name="get_from_path"),
    path('query-args/', get_argument_from_query, name="get_from_query"),
    path('query-type/', check_http_query_type, name="check_query_type"),
    path('get-headers/', get_headers, name="get_headers"),
    path('raise-error/', raise_error_for_fun, name="raise_error"),
    path('author-list/', AuthorListBasedView.as_view(), name="author_list"),
    path('category-list/', CategoryListTemplateView.as_view(), name="category_list"),
    path('books-list/', BookListView.as_view(), name="book_list"),
    path('book-details/<int:pk>/', BookDetailsView.as_view(), name="book_details"),
    path('category-create/', CategoryCreateFormView.as_view(), name="category_create"),
    path('author-create/', AuthorCreateView.as_view(), name="author_create"),
    path('author-update/<int:pk>/', AuthorUpdateView.as_view(), name="author_update"),
    path('book-create/', BookCreateView.as_view(), name="book_create"),
    path('book-update/<int:pk>/', BookUpdateView.as_view(), name="book_update"),
]