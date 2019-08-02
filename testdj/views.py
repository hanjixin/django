from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['name'] = 'Hello World!'
    context['description'] = 'Hello World!'
    return render(request, 'index.htm', context)