from django.shortcuts import render
from django.http import HttpResponse
from .models import DishCategory


# Create your views here.
def index(request):
    categories = DishCategory.objects.filter(is_visible=True)
    for item in categories:
        for dish in item:
            print(dish.name)
        print(item.name)
