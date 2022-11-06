from django.urls import path, include
from student_api import views

urlpatterns = [
    path('students/' , views.StudentListView.as_view()),

    path('student/<int:pk>/' , views.StudentDetailView.as_view()),

    path('studentDelete/<int:pk>/' , views.StudentDeleteView.as_view()),

    path('get-or-post-students/' , views.StudentListCreateView.as_view()),

    path('get-or-update-student/<int:pk>/' , views.StudentDetailUpdateView.as_view())
]
