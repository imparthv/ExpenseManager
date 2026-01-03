from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ExpenseSerializer
from .models import Expenses


class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    # Providing user level isolation 
    def get_queryset(self):
        return Expenses.objects.filter(user=self.request.user)

    # Perform operations for logged in user only
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        return Expenses.objects.filter(user=self.request.user)

        
