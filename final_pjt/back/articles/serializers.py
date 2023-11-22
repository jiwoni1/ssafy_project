from .models import Article, Comment
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user',)


# 게시글 생성, 단일 조회 시 사용
class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'


    comment_set = CommentSerializer(many=True, read_only=True) 
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


# 게시글 전체 조회 시 사용
class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
         class Meta:
            model = User
            fields = '__all__'


    user_set = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'user_set')

