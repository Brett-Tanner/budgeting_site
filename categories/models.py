from django.db import models
from django.urls import reverse
from budgets.models import Budget


class Category(models.Model):
    name = models.CharField(max_length=100)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"pk": self.pk})
