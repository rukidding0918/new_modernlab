from django.contrib import admin
from .models import Herb, Recipe, RecipeHerb


@admin.register(Herb)
class HerbAdmin(admin.ModelAdmin):
    list_display = ["name", "buy_price", "price"]
    list_display_links = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


class RecipeHerbInline(admin.TabularInline):
    model = RecipeHerb


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [
        RecipeHerbInline,
    ]
# TODO 쿼리 줄이기(https://medium.com/chrisjune-13837/%EB%8B%B9%EC%8B%A0%EC%9D%B4-%EB%AA%B0%EB%9E%90%EB%8D%98-django-prefetch-5d7dd0bd7e15)