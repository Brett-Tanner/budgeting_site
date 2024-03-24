from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Budget
from .forms import BudgetForm


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
    form = BudgetForm()

    def post(self, request, *args, **kwargs):
        form = BudgetForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            print(request.user.id)
            print(instance)
            instance.user_id = request.user.id
            print(instance.user)
            print(instance.user_id)
            instance.save()
            return render(request, "budgets/budget.html", {"budget": instance})


class BudgetUpdateView(UpdateView):
    model = Budget
    fields = ["name", "start_date", "end_date", "income"]
    template_name = "budgets/edit.html"


class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = "budgets/delete.html"
    success_url = reverse_lazy("budgets")
