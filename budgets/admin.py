from django.contrib import admin
from .models import Budget
from categories.models import Category


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class BudgetAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


admin.site.register(Budget, BudgetAdmin)
