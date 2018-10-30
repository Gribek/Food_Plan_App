from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    preparation_time = models.IntegerField()
    votes = models.IntegerField()


class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField()
    recipes = models.ManyToManyField(Recipe, through="RecipePlan")


class RecipePlan(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    meal_name = models.CharField(max_length=255)
    order = models.IntegerField()
    day_name = models.ForeignKey("DayName", on_delete=models.SET_NULL,
                                 null=True)


class DayName(models.Model):
    day_name = models.CharField(max_length=16)
    order = models.IntegerField()


class Page(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.CharField(max_length=255)
