from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Transaction


class TransactionListView(ListView):
    model = Transaction
    template_name = "transactions/list.html"


class TransactionCreateView(CreateView):
    model = Transaction
    fields = ["name", "amount", "category"]
    template_name = "transactions/new.html"
    success_url = reverse_lazy("transactions")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(UpdateView):
    model = Transaction
    fields = ["name", "amount", "category"]
    template_name = "transactions/edit.html"
    success_url = reverse_lazy("transactions")


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = "transactions/delete.html"
    success_url = reverse_lazy("transactions")
