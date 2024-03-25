from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Budget


class BudgetListView(ListView):
    model = Budget
    template_name = "budgets/list.html"


class BudgetDetailView(DetailView):
    model = Budget
    template_name = "budgets/budget.html"


class BudgetCreateView(CreateView):
    model = Budget
    fields = ["name", "start_date", "end_date", "income"]
    template_name = "budgets/new.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BudgetUpdateView(UpdateView):
    model = Budget
    fields = ["name", "start_date", "end_date", "income"]
    template_name = "budgets/edit.html"


class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = "budgets/delete.html"
    success_url = reverse_lazy("budgets")
