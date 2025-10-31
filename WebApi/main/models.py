from django.db import models

class ArticlesTypeL(models.Model):
    Title = models.CharField(max_length = 100)
    Description = models.CharField(max_length = 255)

    def __str__(self):
        return self.Title

class ArticleTagsTypeL(models.Model):
    Title = models.CharField(max_length = 100)
    Description = models.CharField(max_length = 255)

    def __str__(self):
        return self.Title

class Article(models.Model):
    Title = models.CharField(max_length  = 100)
    CreateDate = models.DateTimeField(auto_now_add = True)
    UpdateDate = models.DateTimeField(auto_now= True)
    ArticleTypeID = models.ForeignKey("ArticlesTypeL", on_delete=models.CASCADE)
    ArticleTagsID = models.ForeignKey("ArticleTagsTypeL", on_delete=models.CASCADE) 
    Body = models.TextField()
    Thumbnail = models.ImageField(upload_to = 'ArticleImg/',blank = True , null = True)

    def __str__(self):
        return f"{self.Title} - {self.CreateDate}"
