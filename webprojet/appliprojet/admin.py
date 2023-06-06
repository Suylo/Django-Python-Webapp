from django.contrib import admin

# Register your models here.
from appliprojet.models import Posseder, Jeux, Categorie, Selection

admin.site.register(Posseder)
admin.site.register(Jeux)
admin.site.register(Categorie)
admin.site.register(Selection)
