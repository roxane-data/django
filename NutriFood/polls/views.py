#from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey ! Tu es sur l'index de l'application search du projet NutriFood.")
