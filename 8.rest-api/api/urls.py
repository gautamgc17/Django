from django.urls import path , include
from api import views

urlpatterns = [
    path('users/' , views.usersApi),
    path('usersnew/' , views.usersApiNew), 

    path('getArticles/' , views.getArticles),
    path('getArticle/<int:pk>/' , views.getArticle),

    path('createArticle/' , views.createArticleAPI),

    path('articles/' , views.ArticlesListView.as_view()),
    path('article/<int:pk>/' , views.ArticlesDetailView.as_view()),
    path('articlenew/<int:pk>/' , views.ArticlesNewView.as_view()),

    path('create-or-get/' , views.ArticleNewListView.as_view())
]