from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ExpenseSerializer
from .models import Expenses

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import ExpenseFilter

from .pagination import ExpensePagination

# importing timezone
from django.utils import timezone

# Importing sum class to be used along with aggregation
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response


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
    

def fetch_dates():
    today = timezone.now()
    date_dict = {
        "today": today,
        "month_start": today.replace(day=1)
    }

    return date_dict

# View to find total expense made by the user in given date range
# Uses aggregate instead of python loops
class MonthlyExpenseSummaryView(APIView):
    def get(self, request):
       
        date_dict = fetch_dates()

        # Calculating total expense for a given date range
        expense_result = Expenses.objects.filter(user= request.user, 
                                                 created_at__gte = date_dict.get("month_start"), created_at__lte = date_dict.get("today")).aggregate(total_expense = Sum('amount'))

        # Returning response based in month , year and expense
        return Response({
            "month": date_dict.get("today").strftime("%B"),
            "year": date_dict.get("today").strftime("%Y"),
            "total_expense": expense_result.get("total_expense")
        })
    
# View for category-wise expense
class CategoryExpenseSummaryView(APIView):
    def get(self, request):
        date_dict = fetch_dates()

         # Calculating total expense for a given date range
        categorywise_expense= Expenses.objects.filter(user= request.user, 
                                                 created_at__gte = date_dict.get("month_start"), created_at__lte = date_dict.get("today")).values("category").annotate(total_expense = Sum('amount'))
        
        return Response({
            categorywise_expense
        })

        
