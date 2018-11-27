from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.views import View
from datetime import datetime
from random import randint, shuffle
from django.shortcuts import render
from django.views import View


def add_test_data_to_database(request):
    """
    Recipe.objects.create(name="Gulasz", ingredients="mięso, papryka, i kilka innych",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=30)
    Recipe.objects.create(name="Naleśniki", ingredients="mąka, woda, sól, dżem",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=45)
    Recipe.objects.create(name="Gołąbki", ingredients="kapusta, ryż, mięso ",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=240)
    Recipe.objects.create(name="koktajl", ingredients="wszystko co masz pod reką",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=30)
    Recipe.objects.create(name="Kotlet de volaille", ingredients="askhndirygbc elsrghcmdrgd",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=30)
    Recipe.objects.create(name="zapiekanka", ingredients="asfag, sdgvdh, rgdrtgdt, dtrcgtfcgbt",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=30)

    Plan.objects.create(name="jak u mamy", description="pozywny i smaczny")
    Plan.objects.create(name="jak u babci", description="mięsko zjedz ziemniaczki zostaw")
    Plan.objects.create(name="jak u cioci", description="lepiej niż na imieninach")
    Plan.objects.create(name="jak u dziadka", description="dawaj wnuczku na drugą")

    Recipeplan.objects.create(meal_name="śniadanie", order=1, day_name=1, plan_id=1, recipe_id=1)
    Recipeplan.objects.create(meal_name="obiad", order=2, day_name=1, plan_id=1, recipe_id=3)
    Recipeplan.objects.create(meal_name="kolacja", order=3, day_name=1, plan_id=1, recipe_id=4)
    Recipeplan.objects.create(meal_name="śniadanie", order=1, day_name=3, plan_id=2, recipe_id=7)
    Recipeplan.objects.create(meal_name="obiad", order=2, day_name=3, plan_id=2, recipe_id=5)
    Recipeplan.objects.create(meal_name="kolacja", order=3, day_name=3, plan_id=2, recipe_id=2)
    Recipeplan.objects.create(meal_name="śniadanie", order=1, day_name=3, plan_id=2, recipe_id=6)
    Recipeplan.objects.create(meal_name="obiad", order=2, day_name=3, plan_id=3, recipe_id=1)
    Recipeplan.objects.create(meal_name="kolacja", order=3, day_name=3, plan_id=3, recipe_id=2)
"""


class LandingPage(View):

    def get(self, request):
        model_lenght = Recipe.objects.count()
        result = [i for i in range(1, model_lenght)]
        shuffle(result)

        recipe = Recipe.objects.get(pk=result[0])
        recipe2 = Recipe.objects.get(pk=result[1])
        recipe3 = Recipe.objects.get(pk=result[2])

        ctx = {"recipe": recipe,
               "recipe2": recipe2,
               "recipe3": recipe3,
               }

        return render(request, "index.html", ctx)


class Recipe_List(View):

    def get(self, request):
        return render(request, "recipes.html")


class ContactView(View):

    def get(self, request):
        return render(request, "index.html")


class AboutView(View):

    def get(self, request):
        return render(request, "index.html")


class MainPage(View):

    def get(self, request):
        plans_amount = Plan.objects.count()
        recipes_amount = Recipe.objects.count()
        ctx = {
            'plans': plans_amount,
            'recipes': recipes_amount,
        }
        return render(request, "dashboard.html", ctx)
