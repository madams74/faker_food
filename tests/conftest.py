import pytest
from faker import Faker
from faker_food import FoodProvider


@pytest.fixture(scope="session")
def fake():
    fake = Faker()
    fake.add_provider(FoodProvider)
    return fake
