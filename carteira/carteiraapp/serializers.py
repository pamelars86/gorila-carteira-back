from rest_framework import serializers
from .models import Investment

class InvestmentSerializer(serializers.ModelSerializer):
    purchase_date = serializers.DateField(format="%Y/%m/%d")

    class Meta:
        model = Investment
        fields = ('id', 'type_investment', 'amount', 'purchase_date')