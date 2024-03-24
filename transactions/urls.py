from django.urls import path
from .views import (
    TransactionListView,
    TransactionUpdateView,
    TransactionDeleteView,
    TransactionCreateView,
)

urlpatterns = [
    path("", TransactionListView.as_view(), name="transactions"),
    path("<int:pk>/edit/", TransactionUpdateView.as_view(), name="edit_transaction"),
    path(
        "<int:pk>/delete/", TransactionDeleteView.as_view(), name="delete_transaction"
    ),
    path("new/", TransactionCreateView.as_view(), name="new_transaction"),
]
