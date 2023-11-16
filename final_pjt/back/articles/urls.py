from django.urls import path
from . import views


urlpatterns = [
    # 게시글 전체 조회, 생성
    # path('articles/', views.article_list_create),
    # 게시글 단일 조회, 삭제, 수정
    # path('articles/<int:article_pk>/', views.article_detail),
    
    # 댓글 수정, 삭제
    # path('comments/<int:comment_pk>/', views.comment_detail),
    # 댓글 생성
    # path('articles/<int:article_pk>/comments/', views.comment_create),

]
