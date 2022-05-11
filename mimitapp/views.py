
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'mimitapp/registerutilizador.html')


def loginutilizador(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('mimitapp:perfilutilizador'))
        else:
            return render(request, 'mimitapp/registerutilizador.html')
    else:
        return render(request, 'mimitapp/registerutilizador.html')



def guardarregistoutilizador(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('votacao:perfilutilizador'))
