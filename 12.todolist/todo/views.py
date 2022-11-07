from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from todo import models


def index(request):
    todos = models.Todo.objects.all()
    
    if request.method == 'POST':
        new_todo = models.Todo(title = request.POST.get('title'))
        new_todo.save()
        return redirect('/')
    
    return render(request , 'index.html' , context = {'todos': todos})


def delete(request: HttpRequest , pk: str):
    todo_d = models.Todo.objects.get(id = pk)
    todo_d.delete()
    return redirect('/')
