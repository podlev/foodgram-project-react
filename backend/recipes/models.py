from django.contrib.auth import get_user_model
from django.db import models

from colorfield import fields

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        unique=True)
    color = fields.CharField(
        verbose_name='Цвет',
        max_length=7,
        unique=True)
    slug = models.SlugField(
        verbose_name='Слаг',
        max_length=200,
        unique=True
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        unique=True)
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=20,
        unique=True)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    amount = models.IntegerField(
        verbose_name='Количество',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        related_name='recipe_in_ingredient',
        verbose_name='Ингредиент',
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        'Recipe',
        related_name='recipes_ingredients_list',
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
    )


class Recipe(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        unique=True)
    text = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='images/',
        null=True,
        default=None
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги')
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='recipes_author'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through=IngredientRecipe,
        verbose_name='Ингредиенты',
        related_name='ingredients',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name
