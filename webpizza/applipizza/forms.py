from django import forms
from django.forms import ModelForm
from applipizza.models import Ingredient, Pizza

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['nomIngredient']