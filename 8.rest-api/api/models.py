from django.db import models

# Create your models here

class Tags(models.Model):
    name = models.CharField(max_length = 256)
    class Meta:
        verbose_name_plural = "Tags"   
    def __str__(self):
        return self.name


class Article(models.Model):
    slug = models.SlugField(null = True , blank = True)
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField()
    body = models.TextField()
    tags = models.ManyToManyField('Tags' , blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    favourited = models.BooleanField()
    favouriteCount = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Article"
    def __str__(self):
        return self.title

    

