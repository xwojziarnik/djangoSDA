from uuid import uuid4

from django.contrib.auth.decorators import login_required
from django.core.exceptions import BadRequest, PermissionDenied
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from books.forms import CategoryForm, logger, AuthorForm, BookForm
from books.models import BookAuthor, Category, Book
import logging

logger = logging.getLogger("wojtek")

class AuthorListBasedView(View):
    template_name = "author_list.html"
    queryset = BookAuthor.objects.all()  # type: ignore

    def get(self, request: WSGIRequest, *args, **kwargs):
        logger.debug(f"Dupa! {request}")
        context = {"authors": self.queryset}
        return render(request, template_name=self.template_name, context=context)

class CategoryListTemplateView(TemplateView):
    template_name = "category_list.html"
    extra_context = {"categories": Category.objects.all()} # type: ignore

class BookListView(ListView):
    template_name = "books_list.html"
    model = Book
    paginate_by = 10

class BookDetailsView(DetailView):
    template_name = "book_details.html"
    model = Book

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))

class CategoryCreateFormView(FormView):
    template_name = "category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")

    def form_invalid(self, form):
        logger.critical(f"FORM CRITICAL ERROR, MORE INFO: {form}")
        return super().form_invalid(form)

    def form_valid(self, form):
        result = super().form_valid(form)
        logger.info(f"form = {form}")
        logger.info(f"form.cleaned_data = {form.cleaned_data}")  # cleaned means with removed html indicators
        check_entity = Category.objects.create(**form.cleaned_data) #type: ignore
        logger.info(f"check_entity-id={check_entity.id}")
        return result

class AuthorCreateView(CreateView):
    template_name = "author_form.html"
    form_class = AuthorForm
    success_url = reverse_lazy("author_list")

class AuthorUpdateView(UpdateView):
    template_name = "author_form.html"
    form_class = AuthorForm
    success_url = reverse_lazy("author_list")

    def get_object(self, **kwargs):
        return get_object_or_404(BookAuthor, id=self.kwargs.get("pk"))

#zadanie 13
class BookCreateView(CreateView):
    template_name = "book_form.html"
    form_class = BookForm
    # success_url = reverse_lazy("book_list")

    def get_success_url(self):
        return reverse_lazy("book_list")

#zadanie 14

class BookUpdateView(DeleteView):
    template_name = "book_form.html"
    form_class = BookForm
    # success_url = reverse_lazy("book_list")

    def get_success_url(self):
        return reverse_lazy("book_list")

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))

# zadanie 15

class BookDeleteView(DeleteView):
    template_name = "book_delete.html"
    model = Book
    success_url = reverse_lazy("book_list")

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))

#11
@login_required
def get_hello(request: WSGIRequest) -> HttpResponse:
    user: User = request.user  # type: ignore
    # password = None if user.is_anonymous else user.password
    # email = None if user.is_anonymous else user.email
    # date_joined = None if user.is_anonymous else user.date_joined
    # if not user.is_authenticated:
    #     # raise PermissionDenied()
    #     return HttpResponseRedirect(reverse('login'))
    is_auth: bool = user.is_authenticated
    hello = f"Hello {user.username}. That's your password: {user.password}, your email: {user.email} and date you joined: {user.date_joined}"
    return render(request, template_name="hello_world.html", context={"hello_var":hello, "is_authenticated": is_auth})

# 12. Utwórz funkcję zwracającą listę stringów. Stringi niech będą losowym UUID dodawanym do listy. Lista niech posiada 10 elementów.
#
#     a) Zwróć listę jako HTTPResponse (musisz na liście zrobić json.dumps)
#     b) zwróć listę jako JsonResponse

def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return render(request, template_name="uuids_a.html", context={"elements":uuids})
    # return HttpResponse(f"uuids={uuids}")

def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids":uuids})

def get_argument_from_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:
    return HttpResponse(f"x = {x}\ny = {y}\nz = {z}")

def get_argument_from_query(request: WSGIRequest) -> HttpResponse:
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    print(type(int(a)))
    return HttpResponse(f"a = {a}, b = {b}, c = {c}")

@csrf_exempt
def check_http_query_type(request: WSGIRequest) -> HttpResponse:
    # query_type = "unknown"
    # if request.method == "GET":
    #     query_type = "This is GET"
    # elif request.method == "POST":
    #     query_type = "This is POST"
    # elif request.method == "DELETE":
    #     query_type = "This is DELETE"
    # elif request.method == "PUT":
    #     query_type = "This is PUT"
    # return HttpResponse(query_type)
    return render(request, template_name="methods.html",context={})

#zadanie 21 Przygotuj funkcję która zwróci informację o headerach HTTP

def get_headers(request: WSGIRequest) -> JsonResponse:
    our_headers = request.headers
    return JsonResponse({"headers":dict(our_headers)})

# 22. Rzuć wyjątkiem HTTP

@csrf_exempt
def raise_error_for_fun(request: WSGIRequest) -> HttpResponse:
    if request.method != "GET":
        raise BadRequest("Method not allowed")
    return HttpResponse("Everything ok.")

# 23. Dodaj routing w urls projektu do urls aplikacji

