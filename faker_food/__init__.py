from random import choice

from faker.providers import BaseProvider

from .dish_descriptions import dish_descriptions
from .dishes import dishes
from .ethnic_categories import ethnic_categories
from .fruits import fruits
from .ingredients import ingredients
from .measurements import measurement_sizes, measurements, metric_measurements
from .spices import spices
from .sushi import sushi
from .vegetables import vegetables


class FoodProvider(BaseProvider):
    """
    A Provider for vehicle related test data.
    >>> from faker import Faker
    >>> from faker_food import FoodProvider
    >>> fake = Faker()
    >>> fake.add_provider(FoodProvider)
    """

    def dish_description(self):
        return choice(dish_descriptions)

    def dish(self):
        return choice(dishes)

    def ethnic_category(self):
        return choice(ethnic_categories)

    def fruit(self):
        return choice(fruits)

    def ingredient(self):
        return choice(ingredients)

    def measurement(self):
        return choice(measurements)

    def measurement_size(self):
        return choice(measurement_sizes)

    def metric_measurement(self):
        return choice(metric_measurements)

    def spice(self):
        return choice(spices)

    def sushi(self):
        return choice(sushi)

    def vegetable(self):
        return choice(vegetables)
