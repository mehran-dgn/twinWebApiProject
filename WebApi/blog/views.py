from django.shortcuts import render
from .models import ArticlesCategory , ENArticlesCategory , ArticleTags, ENArticleTags ,Article , ENArticle
from .serializers.ArticleSerializers import ArticlesCategorySerializer,ENArticlesCategorySerializer, ArticleTagsSerializer, ENArticleTagsSerializer, ArticlesSerializer,ENArticlesSerializer
from rest_framework import generics
from .helpers.ApiHelpers import CustomPaginationClass

class ArticlesCategoryListAPIView(generics.ListAPIView):
    queryset = ArticlesCategory.objects.filter(parent__isnull = True)
    serializer_class = ArticlesCategorySerializer

class ENArticlesCategoryListAPIView(generics.ListAPIView):
    queryset = ENArticlesCategory.objects.filter(parent__isnull = True)
    serializer_class = ENArticlesCategorySerializer


class ArticleTagsListAPIView(generics.ListAPIView):
    queryset = ArticleTags.objects.all()
    serializer_class = ArticleTagsSerializer

class ENArticleTagsListAPIView(generics.ListAPIView):
    queryset = ENArticleTags.objects.all()
    serializer_class = ENArticleTagsSerializer


class ArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticlesSerializer
    pagination_class = CustomPaginationClass

    def get_queryset(self):
        return Article.objects.all().order_by('-CreateDate')
    

class ENArticleListAPIView(generics.ListAPIView):
    serializer_class = ENArticlesSerializer
    pagination_class = CustomPaginationClass

    def get_queryset(self):
        return ENArticle.objects.all().order_by('-CreateDate')