from django.shortcuts import render , redirect
from django.http import HttpResponse
from urlshortner import models
import uuid

def index(request):
    return render(request , 'index.html')

# create a universally unique identifier for a given link
def create(request):
    if request.method == 'POST':
        link = request.POST['link']

        # print(uuid.uuid4())
        uid = str(uuid.uuid4())[:5]

        new_url = models.URL(link = link , uuid = uid)
        new_url.save()
        return HttpResponse(uid)

# dynamically render the new link
def go(request , pk):
    url_details = models.URL.objects.get(uuid = pk)
    # print(url_details)
    return redirect(url_details.link)
