from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def about(request):
    return HttpResponse('SOBRE')


def contact(request):
    return HttpResponse('CONTATO')
