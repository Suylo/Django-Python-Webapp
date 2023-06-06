from django.shortcuts import render, redirect

from appliprojet.models import Jeux, Categorie, Posseder, Panier, Jeux, LignePanier
from django.contrib.auth.decorators import login_required

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


@login_required
def panier(request):
    panier, created = Panier.objects.get_or_create(utilisateur=request.user)
    lignes_panier = panier.lignepanier_set.all()

    montant_total = 0
    for ligne_panier in lignes_panier:
        montant_total += ligne_panier.jeux.prix * ligne_panier.quantite
    montant_total = round(montant_total, 2)

    context = {
        'panier': panier,
        'lignes_panier': lignes_panier,
        'montant_total': montant_total
    }

    return render(request, 'appliprojet/panier.html', context)

@login_required
def ajouter_au_panier(request, jeux_id):
    panier, created = Panier.objects.get_or_create(utilisateur=request.user)
    jeux = Jeux.objects.get(id_jeux=jeux_id)

    # Vérifier si le jeu est déjà dans le panier
    ligne_panier, created = LignePanier.objects.get_or_create(panier=panier, jeux=jeux)

    # Incrémenter la quantité si le jeu est déjà dans le panier
    if not created:
        ligne_panier.quantite += 1
        ligne_panier.save()

    return redirect('panier')

@login_required
def supprimer_du_panier(request, ligne_panier_id):
    ligne_panier = LignePanier.objects.get(id=ligne_panier_id)
    ligne_panier.delete()

    return redirect('panier')