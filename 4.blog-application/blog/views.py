from django.shortcuts import render , redirect , get_object_or_404 , get_list_or_404
from django.http import HttpRequest , HttpResponse , Http404 , StreamingHttpResponse
from blog import models

def index(request):
     # top 10 latest article
    # queries are lazily executed
    latest_articles = models.Article.objects.all().order_by('-createdAt')[:10]
    context = {
        'latest_articles': latest_articles,
    }
    return render(request , 'blog/index.html', context)

def article(request , pk):
    # try:
    #     article = models.Article.objects.get(pk = pk)  # get by primary key
    # except:
    #     raise Http404()

    # first parameter may be a Model, Manager, or QuerySet object. All other passed arguments are used in the get() query.
    # returns object from model else return 404 error if not found
    article = get_object_or_404(models.Article , pk = pk)
    context = {
        'article': article
    }
    return render(request , 'blog/article.html' , context)

def author(request , pk):
    author = get_object_or_404(models.Author , pk = pk)
    context = {
        'author': author
    }
    return render(request , 'blog/author.html' , context)

def create_article(request):
    authors = models.Author.objects.all()
    context = {
        'authors': authors
    }

    if request.method == 'POST':
        article_data = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content')
        }

        article = models.Article.objects.create(**article_data)
        author = models.Author.objects.filter(name = request.POST.get('author'))  # returns an iterable
        article.authors.set(author)   # accepts an iterable since it is many-to-many field

        # author = models.Author.objects.get(pk = request.POST["author"])   
        # article.author.set([author])

        context["success"] = True

    return render(request , 'blog/create_article.html' , context)
