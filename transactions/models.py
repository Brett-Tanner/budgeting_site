from django.db import models
from django.urls import reverse
from categories.models import Category


class Transaction(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("transaction", kwargs={"pk": self.pk})
