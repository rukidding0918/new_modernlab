from django.urls import path, register_converter

from . import views
# from . import converters


# register_converter(converters.HangulSlugConverter, 'herb_slug')


app_name = "tang"
urlpatterns = [
    path("recipes/", views.recipe_list, name="recipe_list"),
    path("recipes/<str:slug>/", views.recipe_detail, name="recipe_detail"),
    path("herbs/", views.herb_list, name="herb_list"),
    path("herbs/<str:slug>/", views.herb_detail, name="herb_detail"),   
]
