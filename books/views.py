from uuid import uuid4

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def get_hello(request: WSGIRequest) -> HttpResponse:
    return HttpResponse("<h1>hello world</h1>")

# 12. Utwórz funkcję zwracającą listę stringów. Stringi niech będą losowym UUID dodawanym do listy. Lista niech posiada 10 elementów.
#
#     a) Zwróć listę jako HTTPResponse (musisz na liście zrobić json.dumps)
#     b) zwróć listę jako JsonResponse

def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return HttpResponse(f"uuids={uuids}")

def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids":uuids})

def get_argument_from_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:

    return HttpResponse(f"x = {x}\ny = {y}\nz = {z}")