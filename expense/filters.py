import django_filters
from .models import Expenses

# Creating a custom filter to filter based on dates matching the category
class ExpenseFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(
        field_name='created_at', lookup_expr='gte'
    )

    end_date = django_filters.DateFilter(
        field_name='created_at', lookup_expr='lte'
    )

    class Meta:
        model =Expenses
        fields = ['category']