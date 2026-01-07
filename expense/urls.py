from django.urls import path, include
from .views import ExpenseListCreateView, ExpenseDetailView, MonthlyExpenseSummaryView, CategoryExpenseSummaryView

urlpatterns = [
    path('', ExpenseListCreateView.as_view(), name='expense-list'),
    path('<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('dashboard/monthly-summary/', MonthlyExpenseSummaryView.as_view(), name='monthly-expense-summary'),
    path('dashboard/category-summary/', CategoryExpenseSummaryView.as_view(), name='category-expense-summary'),
]