from django.db import models

# Create your models here.

class Investment(models.Model):

    FIXED = 'Fixo'
    VARIABLE = 'Variável'

    TYPE_INVESTMENT_CHOICES = (
        (FIXED, 'Fixo'),
        (VARIABLE, 'Variável'),
    )
    type_investment = models.CharField(max_length=200, choices=TYPE_INVESTMENT_CHOICES)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    purchase_date = models.DateField()