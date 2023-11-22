import requests

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.conf import settings 
from django.http import JsonResponse
from datetime import datetime
from django.utils.dateformat import DateFormat

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions, ExchangeRate
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingProductsSerializer, SavingOptionsSerializer, ExchangeRateSerializer


# 예금 상품, 옵션 데이터 저장
@api_view(['GET'])
def save_deposit_products(request):
    api_key = settings.BANK_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    # 예금 상품 데이터
    for li in response.get('result').get("baseList"):
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'kor_co_nm' : li.get('kor_co_nm').replace('주식회사', ''),
            'fin_prdt_nm' : li.get('fin_prdt_nm'),
            'etc_note' : li.get('etc_note'),
            'join_deny' : li.get('join_deny'),
            'join_member' : li.get('join_member'),
            'join_way' : li.get('join_way'),
            'spcl_cnd' : li.get('spcl_cnd'),
            'dcls_month' : li.get('dcls_month'),
            'mtrt_int' : li.get('mtrt_int'),
            'max_limit' : li.get('max_limit'),
        }

        # 이미 있는 것은 저장 X
        if DepositProducts.objects.filter(fin_prdt_cd=save_data['fin_prdt_cd']).exists():
            continue
        else:
            serializer = DepositProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()


    # 옵션 데이터
    for li in response.get('result').get("optionList"):
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
            'intr_rate' : li.get('intr_rate'),
            'intr_rate2' : li.get('intr_rate2'),
            'save_trm' : li.get('save_trm'),
        }

        if DepositOptions.objects.filter(fin_prdt_cd=save_data['fin_prdt_cd']).exists():
            continue
        else:
            serializer = DepositOptionsSerializer(data=save_data)
            product = get_object_or_404(DepositProducts, fin_prdt_cd=li.get('fin_prdt_cd'))
            if serializer.is_valid(raise_exception=True):
                serializer.save(product=product)

    return Response({'저장': '성공'})


# DB에 저장된 예금 상품, 옵션 목록 출력
@api_view(['GET'])
def deposit_products(request):
    if request.method == 'GET':
        deposit_product_list = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_product_list, many=True)
        return Response(serializer.data)
    

# 적금 상품 데이터 저장
@api_view(['GET'])
def save_saving_products(request):
    api_key = settings.BANK_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    # 적금 상품 데이터
    for li in response.get('result').get("baseList"):
        save_data = {
            'dcls_month' : li.get('dcls_month'),
            'kor_co_nm' : li.get('kor_co_nm').replace('주식회사', ''),
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'fin_prdt_nm' : li.get('fin_prdt_nm'),
            'etc_note' : li.get('etc_note'),
            'join_deny' : li.get('join_deny'),
            'join_member' : li.get('join_member'),
            'join_way' : li.get('join_way'),
            'spcl_cnd' : li.get('spcl_cnd'),
            'mtrt_int' : li.get('mtrt_int'),
            'max_limit' : li.get('max_limit'),
        }

        if SavingProducts.objects.filter(fin_prdt_cd=save_data['fin_prdt_cd']).exists():
            continue
        else:
            serializer = SavingProductsSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    

    # 옵션 데이터
    for li in response.get('result').get("optionList"):
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
            'rsrv_type_nm' : li.get('rsrv_type_nm'),
            'intr_rate' : li.get('intr_rate'),
            'intr_rate2' : li.get('intr_rate2'),
            'save_trm' : li.get('save_trm'),
        }

        if SavingOptions.objects.filter(fin_prdt_cd=save_data['fin_prdt_cd']).exists():
            continue
        else:
            serializer = SavingOptionsSerializer(data=save_data)
            product = get_object_or_404(SavingProducts, fin_prdt_cd=li.get('fin_prdt_cd'))
            if serializer.is_valid(raise_exception=True):
                serializer.save(product=product)

    return Response({'저장': '성공'})

    
# DB에 저장된 적금 상품 목록, 옵션 목록 출력
@api_view(['GET'])
def saving_products(request):
    if request.method == 'GET':
        saving_product_list = SavingProducts.objects.all()
        serializer = SavingProductsSerializer(saving_product_list, many=True)
        return Response(serializer.data)


# 환율 데이터 가져오기
@api_view(['GET'])
def save_exchange_rate(request):
    api_key = settings.EXCHANGE_RATE_API_KEY
    search_date = int(DateFormat(datetime.now()).format('Ymd'))
    url = f' https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate={search_date}&data=AP01'
    response = requests.get(url).json()

    for li in response:
        save_data = {
            'cur_unit': li.get('cur_unit'),                     # 통화코드
            'cur_nm': li.get('cur_nm'),                         # 국가/통화명
            'deal_bas_r': li.get('deal_bas_r').replace(',','')  # 환율
        }
        if ExchangeRate.objects.filter(cur_unit=save_data['cur_unit']).exists():
            continue
        else:
            serializer = ExchangeRateSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    return JsonResponse({'저장': '성공'})


# 환율 데이터 출력
@api_view(['GET'])
def exchange_rate(request):
    if request.method == 'GET':
        exchage_rate_list = ExchangeRate.objects.all()
        serializer = ExchangeRateSerializer(exchage_rate_list, many=True)
        return Response(serializer.data)