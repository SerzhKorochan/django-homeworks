from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def index(request, dish_name):
    ingredients = DATA.get(dish_name)
    servings = int(request.GET.get('servings', 1))

    context = {}

    if ingredients:
        for name, count in ingredients.items():
            ingredients[name] = count * servings

        context['recipe'] = ingredients

    return render(request, 'calculator/index.html', context)
