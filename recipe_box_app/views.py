from django.shortcuts import render
from recipe_box_app.models import Author, Recipe

# Create your views here.
def index(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes':all_recipes})

def recipe_detail_view(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_detail_view(request, author_id):
    current_author = Author.objects.filter(id=author_id).first()
    current_recipe = Recipe.objects.filter(author= current_author)
    return render(request, 'author_detail.html', {'recipes': current_recipe, 'author': current_author})