from django.shortcuts import render

# Create your views here.
from applipizza.models import Pizza
from applipizza.models import Ingredient
from applipizza.models import Composition

from applipizza.forms import IngredientForm


def pizza(request):
    lesPizzas = Pizza.objects.all()
    return render(request, 'applipizza/pizzas.html', {'pizzas': lesPizzas})


def pizzaOnly(request, pizza_id):
    laPizza = Pizza.objects.get(idPizza=pizza_id)
    compo = Composition.objects.filter(pizza = pizza_id)
    ingredients = []
    for com in compo:
        ingredients.append((com.ingredient.nomIngredient, com.quantite))

    return render(request, 'applipizza/pizza.html', {'pizza': laPizza, 'ingredients': ingredients})

def ingredients(request):
    lesIngredients = Ingredient.objects.all()
    return render(request, 'applipizza/ingredients.html', {'ingredients': lesIngredients})


def formulaireCreationIngredient(request):
    formulaire = IngredientForm()

    return render(request, 'applipizza/formCreationIngredient.html', {'form': formulaire})