# Generated by Django 5.0.1 on 2024-01-28 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('cooking_counter', models.PositiveIntegerField(default=0, verbose_name='Кол-во приготовлений')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='RecipeProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveIntegerField(verbose_name='вес (г)')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.product')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(through='recipes.RecipeProducts', to='recipes.product', verbose_name='Продукты'),
        ),
        migrations.AddConstraint(
            model_name='recipeproducts',
            constraint=models.UniqueConstraint(fields=('product', 'recipe'), name='unique_product_for_recipe'),
        ),
    ]