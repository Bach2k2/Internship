from django.urls import path, include
from snippets import views
from rest_framework import renderers
from snippets.views import SnippetViewSet, UserViewSet, BookViewSet
from rest_framework.routers import DefaultRouter

from snippets import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"books", views.BookViewSet, basename="book")
# router.register(r"login", views.LoginView, basename="login")
snippet_list = SnippetViewSet.as_view({"get": "list", "post": "create"})
snippet_detail = SnippetViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)
snippet_highlight = SnippetViewSet.as_view(
    {"get": "highlight"}, renderer_classes=[renderers.StaticHTMLRenderer]
)
user_list = UserViewSet.as_view({"get": "list"})
user_detail = UserViewSet.as_view({"get": "retrieve"})

book_list = BookViewSet.as_view({"get": "list", "post": "create", "delete": "destroy"})


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
    path("snippets/", snippet_list, name="snippet-list"),
    path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
    path("snippets/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"),
    path("users/", user_list, name="user-list"),
    path("users/<int:pk>/", user_detail, name="user-detail"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("books/", book_list, name="book-list"),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
