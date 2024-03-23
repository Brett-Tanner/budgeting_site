from django.forms import ModelForm
from .models import Budget


class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ["name", "start_date", "end_date", "income"]
