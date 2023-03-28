from django.shortcuts import render
from django.http import HttpResponse
import nltk

def home(request):
    text = request.GET.get('text')
    if text:
        if isinstance(text, str):
            tokens = nltk.word_tokenize(text)
            return HttpResponse(tokens)
        else:
            return HttpResponse('Invalid input')
    else:
        return HttpResponse('No input provided')
