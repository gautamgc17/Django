from django.shortcuts import render
from django.views.generic import TemplateView
from services.emojifier import api
import emoji

# Create your views here.
class Index(TemplateView):
    template_name = "index.html"

    def post(self, request):
        content = request.POST['content']
        e = emoji.emojize(api.predict(content))
        context = {
            "content": content,
            "emoji": e
        }
        return render(request, self.template_name, context)


