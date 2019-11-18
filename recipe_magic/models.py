from django.db import models


class User(models.Model)
    user_name = models.CharField(max_length=200)

class Recipe(models.Model):
    user_id = models.ForeignKey(Category, on_delete=models.CASCADE,
    recipe_id ='recipes')
    text = models.TextField()aiufuoiusd