from django.urls import path, include
from main import views

urlpatterns = [
    path('' , views.Index.as_view())
]