from django.conf import settings
from django.db import models
from django.urls import reverse


class Budget(models.Model):
    end_date = models.DateField()
    income = models.IntegerField()
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("budget", kwargs={"pk": self.pk})
