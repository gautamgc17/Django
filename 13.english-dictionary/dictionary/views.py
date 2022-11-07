from django.shortcuts import render , redirect
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request , 'index.html')

def word(request):
    if request.method == 'GET':
        word = request.GET.get('search')
        dict = PyDictionary()
        meaning = dict.meaning(word)
        synonyms = dict.synonym(word)
        antonyms = dict.antonym(word)
        meaningN = meaning.get('Noun')[0]
        # meaningV = meaning.get('Verb')
        # meaningA = meaning.get('Adjective')
        context = {
            'meaningN': meaningN,
            # 'meaningV': meaningV,
            # 'meaningA': meaningA,
            'synonyms': synonyms,
            'antonyms': antonyms
        }
        return render(request , 'index.html' , context)
