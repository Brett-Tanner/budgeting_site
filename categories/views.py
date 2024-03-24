from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = "categories/list.html"


class CategoryCreateView(CreateView):
    model = Category
    fields = ["name", "budget"]
    template_name = "categories/new.html"
    success_url = reverse_lazy("categories")


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name", "budget"]
    template_name = "categories/edit.html"
    success_url = reverse_lazy("categories")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories/delete.html"
    success_url = reverse_lazy("categories")
