from django.urls import path , include
from main import views
# from . import views

urlpatterns = [
    path('languages/' , views.languages , name="languages"),
    path('projects/' , views.projects , name="projectx"),
    path('' , views.index , name="index")   # should be at the end
]

