from django.urls import path
from .views import (
    CategoryListView,
    CategoryUpdateView,
    CategoryDeleteView,
    CategoryCreateView,
)

urlpatterns = [
    path("", CategoryListView.as_view(), name="categories"),
    path("<int:pk>/edit/", CategoryUpdateView.as_view(), name="edit_category"),
    path("<int:pk>/delete/", CategoryDeleteView.as_view(), name="delete_category"),
    path("new/", CategoryCreateView.as_view(), name="new_category"),
]
