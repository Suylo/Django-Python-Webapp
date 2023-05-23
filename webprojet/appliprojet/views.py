from django.shortcuts import render

from appliprojet.models import Jeux


# Create your views here.
def jeux(request):

    jeux = Jeux.objects.all()

    return render(request, 'appliprojet/jeux.html', {'jeux': jeux})
