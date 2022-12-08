# Generated by Django 4.1.3 on 2022-12-08 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_image_alter_recipe_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipes.Amount', to='recipes.ingredient'),
        ),
        migrations.AlterField(
            model_name='amount',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amount_ingredients', to='recipes.recipe', verbose_name='Рецепт'),
        ),
    ]
