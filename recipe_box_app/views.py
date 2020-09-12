from django.shortcuts import render, redirect, reverse
from recipe_box_app.models import Author, Recipe
from recipe_box_app.forms import AddRecipeForm, AddAuthorForm, LoginForm, SignupForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


def index(request):
    all_recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes':all_recipes})


def recipe_detail_view(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def author_detail_view(request, author_id):
    current_author = Author.objects.filter(id=author_id).first()
    current_recipe = Recipe.objects.filter(author=current_author)
    favs_list = current_author.favorite.all()
    return render(request, 'author_detail.html', {'recipes': current_recipe, 'favs_list': favs_list, 'author':current_author})


def add_favorite(request, recipe_id):
    current_user = request.user.author
    favorites = Recipe.objects.filter(id=recipe_id).first()
    current_user.favorite.add(favorites)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "redirect_if_referer_not_found"))


@login_required
def add_recipe(request):
    if request.user.is_staff:
        if request.method == 'POST': 
            form = AddRecipeForm(request.POST)
            if form.is_valid():
                form.save()
        form = AddRecipeForm()
        return render(request, "add_recipe.html", {"form": form})
    else:
        if request.method == 'POST': 
            form = AddRecipeForm(request.POST)
            if form.is_valid():
                form.save()
        form = AddRecipeForm(initial={"author": request.user.author})
        return render(request, "add_recipe.html", {"form": form})


@login_required
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    data = {
        "title": recipe.title,
        "author": recipe.author,
        "description": recipe.description,
        "time_required": recipe.time_required,
        "instructions": recipe.instructions
    }
    if request.user.is_staff or request.user.id == recipe.author.id:
        form = AddRecipeForm(initial=data)
        return render(request, "add_recipe.html", {"form": form})
    else:
        return render(request, "no_access.html")


@login_required
def add_author(request):
    if request.user.is_staff:
        if request.method == 'POST': 
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(username=data.get('username'), password=data.get('password'))
                new_author = form.save(commit=False)
                new_author.user = new_user
                new_author.save()
        form = AddAuthorForm()
        return render(request, "add_author.html", {"form": form})
    else:
        return render(request, "no_access.html")


def signup_view(request):
    if request.method =="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get('firstname').lower() + data.get('lastname').lower()
            new_user = User.objects.create_user(username=username, password=data.get('password'))
            Author.objects.create(name=data.get('firstname').capitalize() + ' ' + data.get('lastname').capitalize(), bio=data.get('bio'), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'add_author.html',  {'form': form})


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
