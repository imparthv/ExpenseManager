from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ExpenseSerializer
from .models import Expenses

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import ExpenseFilter

from .pagination import ExpensePagination

# View to list user expenses
# Only authenticated user/Logged in user can view their expenses
# Providing custom filter functionality to filter based on date and category
# Sorting based on created date and amount
# Custom pagination class
class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = ExpenseFilter # Using Custom filter
    filter_backends = [DjangoFilterBackend, OrderingFilter] # Filtering and Ordering

    # Sorting based on date and amount
    ordering_fields = ['created_at', 'amount']

    # Adding custom pagination
    pagination_class = ExpensePagination

    # Providing user level isolation 
    def get_queryset(self):
        return Expenses.objects.filter(user=self.request.user)

    # Perform operations for logged in user only
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# View to handle update and delete functionalities for a specific expense
class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated] # Ensuring authenticated user only

    # Fetching information of logged in user only
    def get_queryset(self):
        return Expenses.objects.filter(user=self.request.user)
    


        
