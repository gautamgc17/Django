from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView)

from student_api import models , serializers

# GET REQUEST
class StudentListView(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

# GET REQUEST (Single Value)
class StudentDetailView(RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


# DELETE REQUEST
class StudentDeleteView(DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    
# GET OR POST REQUEST
class StudentListCreateView(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


# GET OR PATCH REQUEST
class StudentDetailUpdateView(RetrieveUpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer




