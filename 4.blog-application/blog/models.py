from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 256)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add = True)
    # Provide a many-to-many relation by using an intermediary model that holds two ForeignKey fields pointed at the two sides of the relation.
    authors = models.ManyToManyField('Author')
    def __str__(self):
        return self.title
