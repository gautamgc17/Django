from django.urls import path , include
from HelloWorld import views

urlpatterns = [
    path('' , views.index),
    path('hello' , views.hello),
]