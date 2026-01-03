from django.urls import path, include
from .views import ExpenseListCreateView, ExpenseDetailView

urlpatterns = [
    path('expense/', ExpenseListCreateView.as_view(), name='expense-list'),
    path('expense/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail')
]