from django.shortcuts import render

from appliprojet.models import Jeux, Categorie, Posseder


def all(request):
    jeux = Jeux.objects.all()
    categories = Categorie.objects.all()
    posseder = Posseder.objects.all()

    # foreach categories and append to categories.jeux if jeux is not empty
    for categorie in categories:
        categorie.jeux = []
        for poss in posseder:
            if poss.categorie == categorie:
                categorie.jeux.append(poss.jeux)

    return render(request, 'appliprojet/all.html', {'jeux': jeux, 'categories': categories})

def jeux(request):
    jeux = Jeux.objects.all()

    return render(request, 'appliprojet/jeux.html', {'jeux': jeux})


def jeux_details(request, id_jeux):
    jeux = Jeux.objects.get(id_jeux=id_jeux)

    return render(request, 'appliprojet/jeux_details.html', {'jeux': jeux})

def categories(request):
    categories = Categorie.objects.all()

    posseder = Posseder.objects.all()
    # faire la liaison et donc afficher mon tableau catégories.jeux
    for categorie in categories:
        categorie.jeux = []
        for poss in posseder:
            if poss.categorie == categorie:
                categorie.jeux.append(poss.jeux)

    return render(request, 'appliprojet/categories.html', {'categories': categories})


def categories_jeux(request, id_categorie):
    # get only game from category by id_categorie
    categories = Categorie.objects.get(id_categorie=id_categorie)
    posseder = Posseder.objects.all()
    # faire la liaison et donc afficher mon tableau catégories.jeux
    categories.jeux = []
    for poss in posseder:
        if poss.categorie == categories:
            categories.jeux.append(poss.jeux)

    return render(request, 'appliprojet/categories_jeux.html', {'categories': categories})

