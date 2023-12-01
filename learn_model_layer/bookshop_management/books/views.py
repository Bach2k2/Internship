from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class ListBookView(ListView):
    model = Book

    def get(self, request, *args, **kwargs):
        template_name = "books/list-books.html"  # sẽ được tạo ở phần dưới
        obj = {"books": Book.objects.all()}
        return render(request, template_name, obj)


# Create your views here.
