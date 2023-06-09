# Generated by Django 4.2 on 2023-04-03 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applipizza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('idComposition', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.IntegerField(verbose_name="Quantité de l'ingrédient dans la pizza")),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applipizza.ingredient', verbose_name='Ingrédient de la composition')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applipizza.pizza', verbose_name='Pizza de la composition')),
            ],
            options={
                'unique_together': {('ingredient', 'pizza')},
            },
        ),
    ]
