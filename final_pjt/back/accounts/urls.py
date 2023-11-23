from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.user_data),
    path('', views.users_data),
]
