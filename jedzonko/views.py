from .models import *
from random import shuffle
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
        last_plan = Plan.objects.latest("created")
        recipeplans_list = last_plan.recipeplan_set.all().order_by("day_name", "order")
        day_number = 0
        day_list =[]
        for element in recipeplans_list:
            if element.day_name != day_number:
                day_list.append(element)
                day_number = element.day_name
      
        plans_amount = Plan.objects.count()
        recipes_amount = Recipe.objects.count()
        ctx = {
            'plans': plans_amount,
            'recipes': recipes_amount,
            "last_plan" : last_plan,
            "recipeplans_list" : recipeplans_list,
            "day_list" : day_list,
        }
        return render(request, "dashboard.html", ctx)
     

