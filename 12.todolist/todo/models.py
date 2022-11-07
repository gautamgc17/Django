from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 200)

    class Meta:
        verbose_name_plural = "Todo"
        
    def __str__(self):
        return self.title
