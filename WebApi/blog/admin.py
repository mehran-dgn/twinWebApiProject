from django.contrib import admin
from .models import ArticlesCategory,ENArticlesCategory , ArticleTags, ENArticleTags ,Article, ENArticle


admin.site.register(ArticlesCategory)
admin.site.register(ENArticlesCategory)

admin.site.register(ArticleTags)
admin.site.register(ENArticleTags)

admin.site.register(Article)
admin.site.register(ENArticle)
