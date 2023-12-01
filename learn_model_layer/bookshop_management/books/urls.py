# from django.conf.urls import patterns, url
from django.urls import include, path
from django.contrib import admin
from books.views import (
  ListBookView,
)
app_name = "books"
urlpatterns = [
    path('',ListBookView.as_view(),name="list-books" )
]