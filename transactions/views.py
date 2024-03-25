from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
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


class TransactionUpdateView(UserPassesTestMixin, UpdateView):
    model = Transaction
    fields = ["name", "amount", "category"]
    template_name = "transactions/edit.html"
    success_url = reverse_lazy("transactions")

    def test_func(self):
        return self.request.user == self.get_object().user


class TransactionDeleteView(UserPassesTestMixin, DeleteView):
    model = Transaction
    template_name = "transactions/delete.html"
    success_url = reverse_lazy("transactions")

    def test_func(self):
        return self.request.user == self.get_object().user
