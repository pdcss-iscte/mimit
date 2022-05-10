from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Esta é a página de entrada da Mimit")
