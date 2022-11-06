from django.http import HttpRequest , HttpResponse
from datetime import datetime
from django.utils import timezone , dateformat
import json
from api.serializers import StudentSerializer, ArticleSerializer
from api.models import Article
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView)


# Decorator that converts a function-based view into an APIView subclass
# Takes a list of allowed methods/requests for the view/endpoint as an argument.
@api_view()
def usersApi(request: Request) -> Response: 
    # request object earlier was of type HttpRequest but now it is of type Request (json request api -application/json)   
    users = [
        {
            "name": "person",
            "language": "ruby"
        },
        {
            "name": "person2",
            "language": "rails"
        }
    ]
    return Response(users) 


# Serializers - allow complex data instances to be converted to native Python datatypes that can then be easily rendered into JSON
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        self.timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")


@api_view()
def usersApiNew(request: Request):
    # maybe this will come from database
    student1 = Student("gautam", 1, 95)
    student2 = Student("parth", 2, 85)
    student3 = Student("joji", 4, 90)

    # pass object instance or data in list form
    # pass many=True, otherwise it will try to fetch name attribute from the list rather than each object  
    response = StudentSerializer([student1, student2, student3], many = True)
    # print(response) - StudentSerializer Class
    # print(type(response))
    return Response(response.data) 


# FUNCTION BASED API VIEW TO RETRIEVE DATA
@api_view()
def getArticle(request: Request , pk: int) -> Response:
    article = Article.objects.get(pk = pk)
    response = ArticleSerializer(article)
    print(response.data)
    return Response(response.data)

@api_view()
def getArticles(request: Request) -> Response:
    articles = Article.objects.all()
    response = ArticleSerializer(articles , many = True)
    return Response(response.data)

@api_view(['POST'])
def createArticleAPI(request):
    body = json.loads(request.body)
    response = ArticleSerializer(data = body)

    if response.is_valid():
        inst = response.save()
        # print(type(inst) , '\t' , inst)
        # response = ArticleSerializer(inst)
        # print(response.data)
        return Response(response.data)
    
    return Response(response.errors)
    # print(request.body)
    # return Response({"message": "Lets Golang"})


# CLASS BASED API VIEWS
class ArticlesListView(ListAPIView):       # LIST API VIEW (SIMILAR TO LIST VIEW)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticlesDetailView(RetrieveAPIView):    # GET SINGLE VALUE (SIMILAR TO DETAIL VIEW)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticlesNewView(RetrieveUpdateAPIView): 
    # retrives data for GET request else requires a PATCH request to update data (pass only required chnages in the resource)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleNewListView(ListCreateAPIView):
    # this queryset is ran only once and it is cached, so this cached query is run on all subsequent calls
    # queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # however, this line is run for every subsequent request, so we can update or filter the query based on some parameters
    # This method should always be used rather than accessing self.queryset directly, as self.queryset gets evaluated only once, 
    # and those results are cached for all subsequent requests.
    # You may want to override this if you need to provide different querysets depending on the incoming request.
    # (Eg. return a list of items that is specific to the user)

    def get_queryset(self):
        query = {}
        print(self.request.GET)    # QueryDict {}
        for key, val in self.request.GET.items():
            query[f"{key}__icontains"] = val
        # print(query)
        return Article.objects.filter(**query)





