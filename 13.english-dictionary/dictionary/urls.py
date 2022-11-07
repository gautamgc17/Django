from django.urls import path , include
from dictionary import views

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('word' , views.word , name='search-word'), 
]