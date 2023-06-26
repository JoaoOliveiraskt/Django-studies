from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'João Oliveira',
    })

def sobre(request):
    return render(request, 'temp.html')

def contato(request):
    return HttpResponse('contato')
