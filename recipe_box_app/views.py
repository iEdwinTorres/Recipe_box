from django.shortcuts import render
from recipe_box_app.models import Author, Recipe

# Create your views here.
def index(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes':all_recipes})

def recipe_view(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipe_detail.html', {'recipe': recipe})