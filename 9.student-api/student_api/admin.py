from django.contrib import admin
from student_api import models

# Register your models here.
admin.site.register([
    models.Student,
    models.Institute,
])
