from django.urls import path , include
from blog import views

urlpatterns = [
    path('' , views.index),
    path('article/<int:pk>' , views.article , name = 'get-article'),
    path('author/<int:pk>' , views.author , name = 'get-author'),
    path('create-article' , views.create_article , name = 'create-article') 
]