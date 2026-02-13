from rest_framework import serializers
from ..models import (
    ArticlesCategory, ENArticlesCategory,
    ArticleTags, ENArticleTags,
    Article, ENArticle
)

class ArticlesCategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = ArticlesCategory
        fields = ['id', 'Title', 'Description', 'parent', 'children']

    def get_children(self, obj):
        return ArticlesCategorySerializer(obj.children.all(), many=True).data



class ENArticlesCategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = ENArticlesCategory
        fields = ['id', 'Title', 'Description', 'parent', 'children']

    def get_children(self, obj):
        return ENArticlesCategorySerializer(obj.children.all(), many=True).data



class ArticleTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTags
        fields = ['id', 'Title'] 


class ENArticleTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ENArticleTags
        fields = ['id', 'Title']  



class ArticlesSerializer(serializers.ModelSerializer):
    ArticleCategory = ArticlesCategorySerializer(many=True, read_only=True)
    ArticleTags = ArticleTagsSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        exclude = ['Body']


class ENArticlesSerializer(serializers.ModelSerializer):
    ArticleCategory = ENArticlesCategorySerializer(many=True, read_only=True)
    ArticleTags = ENArticleTagsSerializer(many=True, read_only=True)

    class Meta:
        model = ENArticle
        exclude = ['Body']


class ArticleDetailSerializer(serializers.ModelSerializer):
    ArticleCategory = ArticlesCategorySerializer(many=True, read_only=True)
    ArticleTags = ArticleTagsSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'



class ENArticleDetailSerializer(serializers.ModelSerializer):
    ArticleCategory = ENArticlesCategorySerializer(many=True, read_only=True)
    ArticleTags = ENArticleTagsSerializer(many=True, read_only=True)

    class Meta:
        model = ENArticle
        fields = '__all__'
