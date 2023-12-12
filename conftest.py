import pytest

from apps.product.models import Product, Category
from apps.user.models import User


@pytest.fixture
def category1():
    c = Category(name="Mugs")
    c.save()
    return c


@pytest.fixture
def user1():
    b = User(
        username="poopoopy", first_name="pooya", last_name="loop", password="123678990"
    )
    b.save()
    return b


@pytest.fixture
def product1(user1, category1):
    p = Product(
        designer=user1,
        name="Cute Mug",
        category=category1,
        price=20.99,
        description="Something something something",
    )
    p.save()
    return p
