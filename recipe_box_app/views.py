from django.shortcuts import render, redirect, reverse
from recipe_box_app.models import Author, Recipe
from recipe_box_app.forms import AddRecipeForm, AddAuthorForm, LoginForm
from django.contrib.auth import login, logout, authenticate

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

def add_recipe(request):
    if request.method == 'POST': 
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddRecipeForm()
    return render(request, "add_recipe.html", {"form": form})


def add_author(request):
    if request.method == 'POST': 
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddAuthorForm()
    return render(request, "add_author.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                return redirect(request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, "login_form.html", {"form": form})

    


def logout_view(request):
    logout(request)
    return redirect('homepage')
    