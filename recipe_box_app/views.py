from django.shortcuts import render
from recipe_box_app.models import Author, Recipe

# Create your views here.
def index(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes':all_recipes})
