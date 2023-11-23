from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET', 'PUT'])
def user_data(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 모든 유저 정보 조회
@api_view(['GET'])
def users_data(request):
    users = get_list_or_404(User)
    products_set = set()
    print(request.user)
    # 나이대, 연봉, 재산이 비슷한 사람
    for user in users:
        if abs(user.age - request.user.age) < 7 and abs(user.money - request.user.money) < 10000000 and abs(user.salary - request.user.salary) < 100000000:
            print(user.financial_products)
            if user.financial_products:
                product = set(map(str, user.financial_products.split(',')))
                print(product)
                products_set.update(product)
    print(products_set)
    products = {
        'same_product' : list(products_set)
    }
    return Response(products)

    
