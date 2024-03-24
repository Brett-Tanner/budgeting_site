from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Transaction
from .forms import TransactionForm


class TransactionListView(ListView):
    model = Transaction
    template_name = "transactions/list.html"


class TransactionCreateView(CreateView):
    model = Transaction
    fields = ["name", "amount", "category"]
    template_name = "transactions/new.html"
    form = TransactionForm()

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("transactions")


class TransactionUpdateView(UpdateView):
    model = Transaction
    fields = ["name", "amount", "category"]
    template_name = "transactions/edit.html"
    success_url = reverse_lazy("transactions")


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = "transactions/delete.html"
    success_url = reverse_lazy("transactions")
