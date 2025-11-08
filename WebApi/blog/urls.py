from django.urls import path 
from . import views

urlpatterns = [
    path("getAllCategories/fa/",views.ArticlesCategoryListAPIView.as_view() , name = "articleCategories_fa"),
    path("getAllCategories/en/",views.ENArticlesCategoryListAPIView.as_view() , name="articleCategories_en"),
    path("getLatestArticles/fa/",views.ArticleListAPIView.as_view(), name = "articles_fa"),
    path("getLatestArticles/en/",views.ENArticleListAPIView.as_view(), name = "articles_en"),
    path("getAllArticleTags/fa/",views.ArticleTagsListAPIView.as_view(), name = "articleTags_fa"),
    path("getAllArticleTags/en/",views.ENArticleTagsListAPIView.as_view(), name = "articleTags_en")
]
