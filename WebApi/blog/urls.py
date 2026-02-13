from django.urls import path 
from . import views

urlpatterns = [
    path("getAllCategories/fa/",views.ArticlesCategoryListAPIView.as_view() , name = "articleCategories_fa"),
    path("getAllCategories/en/",views.ENArticlesCategoryListAPIView.as_view() , name="articleCategories_en"),
    path("getLatestArticles/fa/",views.ArticleListAPIView.as_view(), name = "articles_fa"),
    path("getLatestArticles/en/",views.ENArticleListAPIView.as_view(), name = "articles_en"),
    path("getAllArticleTags/fa/",views.ArticleTagsListAPIView.as_view(), name = "articleTags_fa"),
    path("getAllArticleTags/en/",views.ENArticleTagsListAPIView.as_view(), name = "articleTags_en"),
    path("getArticlesByCategoryID/fa/<int:category_id>/",views.ArticlesByCategoryAPIView.as_view(),name="articles_by_category_fa"),
    path("getArticlesByCategoryID/en/<int:category_id>/",views.ENArticlesByCategoryAPIView.as_view(),name="articles_by_category_en"),
    path(
    "getArticleDetail/fa/<int:id>/",
    views.ArticleDetailAPIView.as_view(),
    name="article_detail_fa"
),

path(
    "getArticleDetail/en/<int:id>/",
    views.ENArticleDetailAPIView.as_view(),
    name="article_detail_en"
)

]
