from django.urls import path
from . import views

urlpatterns = [
    # 정기예금 데이터 db에 저장
    path('save-deposit-products/', views.save_deposit_products),
    # 정기예금 데이터 가져오기
    path('deposit-products/', views.deposit_products),
    
    # 정기적금 데이터 db에 저장
    path('save-saving-products/', views.save_saving_products),
    # 정기적금 상품목록 가져오기
    path('saving-products/', views.saving_products),

    # 환율 정보 가져오기
    # path('exchange-rate/', views.exchange_rate),

    # 은행 위치정보 가져오기
    # path('find-bankmap/', views.find_bankmap),
]
