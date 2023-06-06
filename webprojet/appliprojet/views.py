from django.shortcuts import render

from appliprojet.models import Jeux, Categorie


def jeux(request):
    jeux = Jeux.objects.all()

    return render(request, 'appliprojet/jeux.html', {'jeux': jeux})


def categories(request):
    categories = Categorie.objects.all()

    return render(request, 'appliprojet/categories.html', {'categories': categories})
