from django.contrib import admin
from .models import Category
from transactions.models import Transaction


class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [TransactionInline]


admin.site.register(Category, CategoryAdmin)
