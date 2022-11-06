from django.db import models

# Create your models here.
class URL(models.Model):
    link = models.CharField(max_length = 1000)
    uuid = models.CharField(max_length = 20)

    class Meta:
        verbose_name_plural = "URL"

    def __str__(self):
        return str(self.pk)

    
