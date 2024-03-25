from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Budget


class BudgetListView(ListView):
    model = Budget
    template_name = "budgets/list.html"

    # def get_queryset(self):
    #     return Budget.objects.filter(user=self.request.user)


class BudgetDetailView(UserPassesTestMixin, DetailView):
    model = Budget
    template_name = "budgets/budget.html"

    def test_func(self):
        return self.request.user == self.get_object().user


class BudgetCreateView(CreateView):
    model = Budget
    fields = ["name", "start_date", "end_date", "income"]
    template_name = "budgets/new.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BudgetUpdateView(UserPassesTestMixin, UpdateView):
    model = Budget
    fields = ["name", "start_date", "end_date", "income"]
    template_name = "budgets/edit.html"

    def test_func(self):
        return self.request.user == self.get_object().user


class BudgetDeleteView(UserPassesTestMixin, DeleteView):
    model = Budget
    template_name = "budgets/delete.html"
    success_url = reverse_lazy("budgets")

    def test_func(self):
        return self.request.user == self.get_object().user
