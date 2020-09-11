"""recipe_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipe_box_app import views


urlpatterns = [
    path("", views.index, name="homepage"),
    path("recipe/<int:recipe_id>/", views.recipe_detail_view),
    path("edit/<int:recipe_id>/", views.edit_recipe),
    path("author/<int:author_id>/", views.author_detail_view),
    path("addauthor/", views.add_author),
    path("addrecipe/", views.add_recipe),
    path("login/", views.login_view, name="loginview"),
    path("signup/", views.signup_view, name="signup"),
    path("noaccess/", views.add_author, name="noaccess"),
    path("logout/", views.logout_view, name="logoutview"),
    path("favorites/<int:user_id>/", views.favorites_view),
    path("addfav/<int:recipe_id>/", views.add_favorite),
    path("admin/", admin.site.urls),
]
