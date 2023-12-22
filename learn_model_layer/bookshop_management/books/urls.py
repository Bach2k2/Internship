# from django.conf.urls import patterns, url
from django.urls import include, path
from django.contrib import admin
from books.views import (
    ListBookView,
)
from . import views 
from .views import UserRegisterView

app_name = "books"
urlpatterns = [

    path('api/books/', views.book_list),
    path('api/books/<int:pk>', views.book_detail),
    # path("api/", include("rest_framework.urls", namespace="rest_framework")),
    path('register',views.UserRegisterView.as_view(),name="register"),
]
