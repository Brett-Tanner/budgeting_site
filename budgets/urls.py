from django.urls import path
from .views import (
    BudgetListView,
    BudgetDetailView,
    BudgetUpdateView,
    BudgetDeleteView,
    BudgetCreateView,
)

urlpatterns = [
    path("", BudgetListView.as_view(), name="budgets"),
    path("<int:pk>/", BudgetDetailView.as_view(), name="budget"),
    path("<int:pk>/edit/", BudgetUpdateView.as_view(), name="edit_budget"),
    path("<int:pk>/delete/", BudgetDeleteView.as_view(), name="delete_budget"),
    path("new/", BudgetCreateView.as_view(), name="new_budget"),
]
