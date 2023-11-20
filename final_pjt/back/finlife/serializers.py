from rest_framework import serializers
from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions, ExchangeRate

class DepositOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

class DepositProductsSerializer(serializers.ModelSerializer):
    depositoptions_set = DepositOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProducts
        fields = '__all__'

# class GetDepositOptionsSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = DepositOptions
#         exclude = ('fin_prdt_cd',)
#         read_only_fields = ('product',)



class SavingOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)

class SavingProductsSerializer(serializers.ModelSerializer):
    savingoptions_set = SavingOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = SavingProducts
        fields = '__all__'

# class GetSavingOptionsSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = SavingOptions
#         exclude = ('fin_prdt_cd',)
#         read_only_fields = ('product',)


# 환율
class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'
