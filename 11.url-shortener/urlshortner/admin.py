from django.contrib import admin
from urlshortner import models

# Register your models here
admin.site.register([
    models.URL,
])
