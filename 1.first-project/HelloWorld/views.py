from django.shortcuts import render
from django.http import HttpResponse

# def welcome(request):
#     # return only HTTP response with string as content
#     return HttpResponse("Welocome User to Dubai!!")


def hello(request):
    return render(request , 'HelloWorld/hello.html')


def index(request):
    developer = 'Josh Starc'
    mentors = [
        'abcd','efgh','hfbf','bbdcu','cxjbx'
    ]
    context = {
        'developer': developer,
        'mentors': mentors
    }
    # render html file with HttpResponse content
    response = render(request , 'HelloWorld/index.html' , context)
    return response

