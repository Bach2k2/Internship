from django.urls import path
from . import views

app_name = "novels"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:novel_id>/", views.detail, name="detail"),      # ex: /novels/5/
    path("create_novel", views.create_novel, name="create_novel"),
]