from .models import *
from random import shuffle
from django.shortcuts import render
from django.views import View


class IndexView(View):

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


def add_test_data_to_database(request):
    Plan.objects.create(name="Domowa", description="Niezbyt zdrowa")

    # Recipe.objects.create(name="Naleśniki", ingredients="mąka, woda, sól, dżem",
    #                       description="to jest opis przepisu",
    #                       preparation_time=45)
    # Recipe.objects.create(name="Gołąbki", ingredients="kapusta, ryż, mięso ",
    #                       description="to jest opis przepisu",
    #                       preparation_time=120)
    # Recipe.objects.create(name="koktajl", ingredients="wszystko co masz pod reką",
    #                       description="to jest opis przepisu",
    #                       preparation_time=30)
    # Recipe.objects.create(name="Kotlet de volaille", ingredients="Pierś z kurczaka, jajko, ser",
    #                       description="to jest opis przepisu",
    #                       preparation_time=120)
    # Recipe.objects.create(name="zapiekanka", ingredients="bułka, ser, pieczarki, salami",
    #                       description="to jest opis przepisu",
    #                       preparation_time=30)
        

class LandingPage(View):

    def get(self, request):
        return render(request, "index.html")

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
        ctx = {"last_plan" : last_plan,
               "recipeplans_list" : recipeplans_list,
               "day_list" : day_list
               }
        return render(request, "dashboard.html", ctx)

