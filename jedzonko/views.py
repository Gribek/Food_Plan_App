from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.views import View
from datetime import datetime
from random import randint, shuffle
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
        return render(request, "dashboard.html")

