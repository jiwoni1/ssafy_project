from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.conf import settings 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import DepositOptions, DepositProducts, SavingProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, GetOptionsSerializer, SavingProductsSerializer


# 예금 상품 데이터 저장
@api_view(['GET'])
def save_deposit_products(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    for li in response.get('result').get("baseList"):
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'kor_co_nm' : li.get('kor_co_nm'),
            'fin_prdt_nm' : li.get('fin_prdt_nm'),
            'etc_note' : li.get('etc_note'),
            'join_deny' : li.get('join_deny'),
            'join_member' : li.get('join_member'),
            'join_way' : li.get('join_way'),
            'spcl_cnd' : li.get('spcl_cnd'),
        }
    
        if DepositProducts.objects.filter(fin_prdt_cd=save_data['fin_prdt_cd']).exists():
            continue
        else:
            # 저장하기 위해 포장
            serializer = DepositProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    return Response({'저장': '성공'})


# DB에 저장된 예금 상품 목록 받아오기
@api_view(['GET'])
def deposit_products(request):
    if request.method == 'GET':
        deposit_product_list = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_product_list, many=True)
        return Response(serializer.data)
    

# 적금 상품 데이터 저장
@api_view(['GET'])
def save_saving_products(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    for li in response.get('result').get("baseList"):

        save_data = {
            'dcls_month' : li.get('dcls_month'),
            'kor_co_nm' : li.get('kor_co_nm'),
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'fin_prdt_nm' : li.get('fin_prdt_nm'),
            'etc_note' : li.get('etc_note'),
            'join_deny' : li.get('join_deny'),
            'join_member' : li.get('join_member'),
            'join_way' : li.get('join_way'),
            'spcl_cnd' : li.get('spcl_cnd'),
        }

        if SavingProducts.objects.filter(fin_prdt_cd=save_data['fin_prdt_cd']).exists():
            continue
        else:
            # 저장하기 위해 포장
            serializer = SavingProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    
    return Response({'저장': '성공'})
    

# DB에 저장된 적금 상품 목록 받아오기
@api_view(['GET'])
def saving_products(request):
    if request.method == 'GET':
        saving_product_list = SavingProducts.objects.all()
        serializer = SavingProductsSerializer(saving_product_list, many=True)
        return Response(serializer.data)