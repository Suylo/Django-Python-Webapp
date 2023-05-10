from django.db import models

# Create your models here.
class Ingredient(models.Model):
    # idIngredient est clé primaire, un auto increment => AutoField
    idIngredient = models.AutoField(primary_key=True)

    # nomIngredient est une chaine de caractère => CharField
    nomIngredient = models.CharField(max_length=50, verbose_name="Nom de l'ingrédient")

    # une méthode de type toString
    def __str__(self) -> str:
        return self.nomIngredient


class Pizza(models.Model):
    # id, nom, prix
    idPizza = models.AutoField(primary_key=True)

    nomPizza = models.CharField(max_length=50, verbose_name="Nom de la pizza")

    prixPizza = models.FloatField(verbose_name="Prix de la pizza")

    # toString
    def __str__(self) -> str:
        return  self.nomPizza + (' | (Prix= ' + str(self.prixPizza) + '€')

class Composition(models.Model):
    class Meta :
        unique_together = ('ingredient', 'pizza')

    # id, ingredient, pizza, quantite
    idComposition = models.AutoField(primary_key=True)

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name="Ingrédient de la composition")

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, verbose_name="Pizza de la composition")

    quantite = models.IntegerField(verbose_name="Quantité de l'ingrédient dans la pizza")

    # toString
    def __str__(self) -> str:
        ing = self.ingredient
        piz = self.pizza
        return ing.__str__() + ' fait partie de ' + piz.__str__() + ' en quantité de ' + str(self.quantite)
