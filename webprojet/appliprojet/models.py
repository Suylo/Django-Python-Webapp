from django.db import models


class Categorie(models.Model):
    id_categorie = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50, verbose_name='Nom de la catégorie')

    def __str__(self):
        return self.nom


class Selection(models.Model):
    id_selection = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=50, verbose_name='Titre de la sélection')

    def __str__(self):
        return self.titre


class Jeux(models.Model):
    id_jeux = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255, verbose_name='Nom du jeu')
    img_url = models.ImageField(verbose_name='Url image', upload_to='images/', max_length=255)
    prix = models.FloatField(verbose_name='Prix du jeu')
    selection = models.ForeignKey(Selection, on_delete=models.CASCADE)

    def __str__(self):
        return self.label


class Posseder(models.Model):
    jeux = models.ForeignKey(Jeux, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return f"Jeux: {self.jeux.label} | Categorie: {self.categorie.nom}"
