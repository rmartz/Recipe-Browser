# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_ingredient_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optional', models.BooleanField(default=False)),
                ('quantity', models.CharField(max_length=32)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients_new',
            field=models.ManyToManyField(related_name='recipes_new', through='recipes.RecipeIngredient', to='recipes.Ingredient'),
        ),
    ]
