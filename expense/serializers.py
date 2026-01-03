from rest_framework import serializers
from .models import Expenses

# Serializer for Expense CRUD

class ExpenseSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d-%m-%Y %I:%M %p",
        read_only=True
    )

    class Meta:
        model = Expenses
        fields = [
            'user', 'amount', 
            'category', 'description',
            'created_at',
        ]