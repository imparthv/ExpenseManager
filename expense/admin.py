from django.contrib import admin
from .models import Expenses

@admin.register(Expenses)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('description','user__username')
