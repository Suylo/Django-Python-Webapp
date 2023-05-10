from django.shortcuts import render

# Create your views here.
from applipizza.models import Pizza
from applipizza.models import Ingredient
from applipizza.models import Composition

from applipizza.forms import IngredientForm
from applipizza.forms import PizzaForm
from applipizza.forms import CompositionForm


def pizza(request):
    lesPizzas = Pizza.objects.all()
    return render(request, 'applipizza/pizzas.html', {'pizzas': lesPizzas})


def pizzaOnly(request, pizza_id):

    formulaire = CompositionForm()

    laPizza = Pizza.objects.get(idPizza=pizza_id)
    compo = Composition.objects.filter(pizza = pizza_id)
    ingredients = []

    for com in compo:
        ingredients.append((com.ingredient.nomIngredient, com.quantite))

    return render(request, 'applipizza/pizza.html', {'pizza': laPizza, 'ingredients': ingredients, "form": formulaire})

def ingredients(request):
    lesIngredients = Ingredient.objects.all()
    return render(request, 'applipizza/ingredients.html', {'ingredients': lesIngredients})


def formulaireCreationIngredient(request):
    formulaire = IngredientForm()
    return render(request, 'applipizza/formCreationIngredient.html', {'form': formulaire})

def creerIngredient(request):
    form = IngredientForm(request.POST)

    if form.is_valid():
        nomIng = form.cleaned_data['nomIngredient']

        ing = Ingredient()
        ing.nomIngredient = nomIng
        ing.save()

        return render(request, "applipizza/traitementFormulaireCreationIngredient.html", {"nom": nomIng})

def formulaireCreationPizza(request):
    formulaire = PizzaForm()
    return render(request, 'applipizza/formCreationPizza.html', {'form': formulaire})

def creerPizza(request):
    form = PizzaForm(request.POST)

    if form.is_valid():
        nomPizza = form.cleaned_data['nomPizza']
        prixPizza = form.cleaned_data['prixPizza']

        piz = Pizza()
        piz.nomPizza = nomPizza
        piz.prixPizza = prixPizza
        piz.save()

        return render(request, "applipizza/traitementFormulaireCreationPizza.html", {"nom": nomPizza, "prix": prixPizza})

def ajouterIngredientDansPizza(request, pizza_id):
    form = CompositionForm(request.POST)

    if form.is_valid():
        ing = form.cleaned_data['ingredient']
        quantite = form.cleaned_data['quantite']

        compo = Composition()
        compo.ingredient = Ingredient.objects.get(idIngredient = ing.idIngredient)
        compo.pizza = Pizza.objects.get(idPizza = pizza_id)
        compo.quantite = quantite
        compo.save()

    formulaire = CompositionForm()

    laPizza = Pizza.objects.get(idPizza = pizza_id)
    compo = Composition.objects.filter(pizza = pizza_id)

    ingredients = []
    for c in compo:
        ing = Ingredient.objects.get(idIngredient = c.ingredient.idIngredient)
        ingredients.append({"nom": ing.nomIngredient, "qte": c.quantite})

    return render(request, 'applipizza/pizza.html', {'pizza': laPizza, 'ingredients': ingredients, "form": formulaire})
