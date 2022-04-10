"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from books.views import get_hello

urlpatterns = [
    path('', get_hello),
    path('books/', include('books.urls'))
    # path('uuids-a', get_uuids_a),
    # path('uuids-b', get_uuids_b),
    # path('path-args/<int:x>/<str:y>/<slug:z>/', get_argument_from_path, name="get_from_path"),
    # path('query-args/', get_argument_from_query, name="get_from_query"),
    # path('query-type/', check_http_query_type, name="check_query_type"),
    # path('get-headers/', get_headers, name="get_headers"),
    # path('raise-error/', raise_error_for_fun, name="raise_error"),
]

if settings.DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))