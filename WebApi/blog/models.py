from django.db import models

class ArticlesCategory(models.Model):
    Title = models.CharField(max_length = 100)
    Description = models.CharField(max_length = 255, blank = True , null = True)

    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE , 
        related_name = "children" , blank = True , null = True
    )


    def __str__(self):
        return self.Title

class ArticleTags(models.Model):
    Title = models.CharField(max_length = 100)
    Description = models.CharField(max_length = 255 , blank=True , null = True) 

    def __str__(self):
        return self.Title
    
    

class Article(models.Model):
    Title = models.CharField(max_length  = 100)
    CreateDate = models.DateTimeField(auto_now_add = True)
    UpdateDate = models.DateTimeField(auto_now= True)

    ArticleCategory = models.ManyToManyField(ArticlesCategory, related_name = "article_cat_fa")
    ArticleTags =   models.ManyToManyField(ArticleTags , related_name = "article_tag_fa") 

    Body = models.TextField()
    Thumbnail = models.ImageField(upload_to = 'ArticleImg/',blank = True , null = True)

    def __str__(self):
        return f"{self.Title} - {self.CreateDate}"   

class ENArticlesCategory(models.Model):
    Title = models.CharField(max_length = 100)
    Description = models.CharField(max_length = 255, blank = True , null = True)

    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE , 
        related_name = "children" , blank = True , null = True
    )


    def __str__(self):
        return self.Title

class ENArticleTags(models.Model):
    Title = models.CharField(max_length = 100)
    Description = models.CharField(max_length = 255 , blank=True , null = True) 

    def __str__(self):
        return self.Title


class ENArticle(models.Model):
    Title = models.CharField(max_length  = 100)
    CreateDate = models.DateTimeField(auto_now_add = True)
    UpdateDate = models.DateTimeField(auto_now= True)

    ArticleCategory = models.ManyToManyField(ENArticlesCategory, related_name = "article_cat_en")
    ArticleTags =   models.ManyToManyField(ENArticleTags , related_name = "article_tag_en") 
    
    Body = models.TextField()
    Thumbnail = models.ImageField(upload_to = 'EN_ArticleImg/',blank = True , null = True)

    def __str__(self):
        return f"{self.Title} - {self.CreateDate}"    
