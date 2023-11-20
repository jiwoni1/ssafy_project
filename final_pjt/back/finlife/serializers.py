from rest_framework import serializers
from .models import DepositOptions, DepositProducts, SavingProducts

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

class GetOptionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DepositOptions
        exclude = ('fin_prdt_cd',)
        read_only_fields = ('product',)

class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'
