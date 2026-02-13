from django.shortcuts import render
from .models import ArticlesCategory , ENArticlesCategory , ArticleTags, ENArticleTags ,Article , ENArticle
from .serializers.ArticleSerializers import ArticlesCategorySerializer,ENArticlesCategorySerializer, ArticleTagsSerializer, ENArticleTagsSerializer, ArticlesSerializer,ENArticlesSerializer , ArticleDetailSerializer , ENArticleDetailSerializer
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


class ArticlesByCategoryAPIView(generics.ListAPIView):
    serializer_class = ArticlesSerializer
    

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Article.objects.filter(
            ArticleCategory__id=category_id
        ).order_by('-CreateDate')


class ENArticlesByCategoryAPIView(generics.ListAPIView):
    serializer_class = ENArticlesSerializer
    

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return ENArticle.objects.filter(
            ArticleCategory__id=category_id
        ).order_by('-CreateDate')


class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'id'


class ENArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = ENArticle.objects.all()
    serializer_class = ENArticleDetailSerializer
    lookup_field = 'id'
