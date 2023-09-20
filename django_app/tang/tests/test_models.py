import math
import random

import pytest

from .factories import HerbFactory


pytestmark = pytest.mark.django_db


def test_herb_str():
    herb = HerbFactory(name="Test Herb")
    assert herb.__str__() == "Test Herb"

def test_herb_price():
    buy_price = random.randint(7000, 40000)
    herb = HerbFactory(buy_price=buy_price)
    assert herb.price == math.ceil(herb.buy_price / herb.buy_unit * (1 + herb.margin / 100))

def test_herb_get_absolute_url():
    herb = HerbFactory()
    assert herb.get_absolute_url() == f"/tang/herbs/{herb.slug}/"