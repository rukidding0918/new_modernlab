from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Herb, Recipe


class RecipeListView(ListView):
    model = Recipe

recipe_list = RecipeListView.as_view()


class RecipeDetailView(DetailView):
    model = Recipe

recipe_detail = RecipeDetailView.as_view()


class HerbListView(ListView):
    model = Herb

herb_list = HerbListView.as_view()


class HerbDetailView(DetailView):
    model = Herb

herb_detail = HerbDetailView.as_view()