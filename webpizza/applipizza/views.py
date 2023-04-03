from django.shortcuts import render

# Create your views here.
from applipizzas.models import Pizza

def pizza(request):
    pizzas = Pizza.objects.all()
    return render(request, 'applipizza/pizzas.html', {'pizzas': pizzas})
