from django.urls import path , include
from urlshortner import views

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('create' , views.create , name = 'create'), 
    # this is a dynamic url
    path('<str:pk>' , views.go , name = 'go'),
]