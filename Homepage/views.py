from django.shortcuts import render
from PyDictionary import PyDictionary
import requests
# Create your views here.
def index(request):
    return render(request,'HomePage.html')

def word(request):
    search = request.GET.get('search')
    dictionary=PyDictionary()
    meanings=dictionary.meaning(search)
    synonyms=dictionary.synonym(search)
    antonyms=dictionary.antonym(search)
    context={
        'word':search,
        'meanings':meanings['Noun'],
        'synonyms':synonyms,
        'antonyms':antonyms
    }
    return render(request,'word.html',context)

