from .models import Article, Comment
from rest_framework import serializers

# 게시글 생성 시 사용
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


# 게시글 조회 시 사용
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


class CommentSerializer(serializers.ModelSerializer):
    class Mate:
        model = Comment
        fields = '__all__'
        read_only_field = ('article',)