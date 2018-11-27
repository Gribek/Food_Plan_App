from django.shortcuts import render, HttpResponse, redirect
from .models import *
from random import shuffle
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def add_test_data_to_database(request):
    """
    Recipe.objects.create(name="Gulasz", ingredients="mięso, papryka, i kilka innych",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=30, votes=99)
    Recipe.objects.create(name="Naleśniki", ingredients="mąka, woda, sól, dżem",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=45, votes=99)
    Recipe.objects.create(name="Gołąbki", ingredients="kapusta, ryż, mięso ",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=240, votes=99)
    Recipe.objects.create(name="koktajl", ingredients="wszystko co masz pod reką",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=30, votes=99)
    Recipe.objects.create(name="Kotlet de volaille", ingredients="askhndirygbc elsrghcmdrgd",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=30, votes=99)
    Recipe.objects.create(name="zapiekanka", ingredients="asfag, sdgvdh, rgdrtgdt, dtrcgtfcgbt",
                          description="shdbdicnsidyfgnciudygfcyugnifyseivfumxsyerifsrxmirybg",
                          preparation_time=30, votes=99)

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
        recipes = Recipe.objects.all().order_by("-votes", "-created")

        paginator = Paginator(recipes, 5)
        page = request.GET.get('page')

        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)     #jeśli nr strony nie będzie liczbą przekieruje na stronę nr 1
        except EmptyPage:       #jeśli nr strony nie będzie przekieruje nas na ostatnią stronę
            items = paginator.page(paginator.num_pages) #num_pages - całkowita liczba stron

        index = items.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 5 if index >= 5 else 0
        end_index = index + 5 if index <= max_index - 5 else max_index
        page_range = paginator.page_range[start_index:end_index]


        ctx = {
            'recipes': recipes,
            'page_range': page_range,
            'items': items,
        }
        return render(request, "recipes.html", ctx)


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
