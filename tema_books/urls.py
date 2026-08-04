from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="tema_books_home"),
    path("ordered_names/", views.ordered_names, name="ordered_names"),
    path("ordered_numbers/", views.ordered_numbers, name="ordered_numbers"),
    path("paired_names/", views.paired_names, name="paired_names"),
]