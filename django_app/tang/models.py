import math
from typing import Collection, Optional

from django.db import models
from django.shortcuts import resolve_url


# Create your models here.
class Herb(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(allow_unicode=True, unique=True, null=False, blank=False)
    buy_price = models.PositiveSmallIntegerField(default=1)
    buy_unit = models.PositiveSmallIntegerField(default=600)
    margin = models.PositiveSmallIntegerField(default=30)

    def __str__(self):
        return self.name

    @property
    def price(self):
        return math.ceil(self.buy_price / self.buy_unit * (1 + self.margin / 100))

    # TODO 하드코딩 개선하기 -> test_herb_get_absolute_url 개선하기
    def get_absolute_url(self):
        return f"/tang/herbs/{self.slug}/"

    def save(self, *args, **kwargs):
        self.slug = self.name
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "약재"


class Recipe(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(allow_unicode=True, unique=True, null=False, blank=False)
    herbs = models.ManyToManyField(Herb, related_name="recipe", through="RecipeHerb")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = "처방전"


class RecipeHerb(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    herb = models.ForeignKey(Herb, on_delete=models.CASCADE)
    herb_amount = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.herb} {self.herb_amount}g"

    class Meta:
        verbose_name_plural = "처방전 구성"
        constraints = [
            models.UniqueConstraint(
                fields=["recipe", "herb"], name="unique_recipe_herb"
            )
        ]