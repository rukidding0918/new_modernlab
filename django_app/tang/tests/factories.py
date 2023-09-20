from django.template.defaultfilters import slugify

import factory
import factory.fuzzy
from ..models import Herb, Recipe, RecipeHerb


class HerbFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText(length=2, chars="가나다라마바사아자차카타파하알록달록무지개", prefix="테")
    slug = factory.LazyAttribute(lambda obj: obj.name)
    buy_price = factory.fuzzy.FuzzyInteger(6000, 32000)
    buy_unit = 600
    margin = 30

    class Meta:
        model = Herb


class RecipeFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText(
        length=2, chars="가나다라마바사아자차카타파하알록달록무지개", prefix="테", suffix="탕"
    )
    slug = factory.LazyAttribute(lambda obj: obj.name)

    class Meta:
        model = Recipe


class RecipeHerbFactory(factory.django.DjangoModelFactory):
    recipe = factory.SubFactory(RecipeFactory)
    herb = factory.SubFactory(HerbFactory)
    herb_amount = factory.fuzzy.FuzzyInteger(2, 10)

    class Meta:
        model = RecipeHerb


class RecipeWith3HerbsFactory(RecipeFactory):
    @factory.post_generation
    def herbs(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for herb in extracted:
                RecipeHerbFactory(recipe=self, herb=herb)
        else:
            RecipeHerbFactory(recipe=self)
            RecipeHerbFactory(recipe=self)
            RecipeHerbFactory(recipe=self)
