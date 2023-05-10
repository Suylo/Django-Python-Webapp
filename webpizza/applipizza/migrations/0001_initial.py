# Generated by Django 4.2 on 2023-04-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('idIngredient', models.AutoField(primary_key=True, serialize=False)),
                ('nomIngredient', models.CharField(max_length=50, verbose_name="Nom de l'ingrédient")),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('idPizza', models.AutoField(primary_key=True, serialize=False)),
                ('nomPizza', models.CharField(max_length=50, verbose_name='Nom de la pizza')),
                ('prixPizza', models.FloatField(verbose_name='Prix de la pizza')),
            ],
        ),
    ]