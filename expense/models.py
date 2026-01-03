from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.


CATEGORY_CHOICES = (
        ('FOOD', 'Food'),
        ('TRAVEL', 'Travel'),
        ('RENT', 'Rent'),
        ('UTILITIES', 'Utilities'),
        ('OTHER', 'Other'),
    )
class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2, 
                                 validators=[MinValueValidator(Decimal('0.01'))])
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.amount}"
