def test_dishes(fake):
    test_dish = fake.dish()
    assert len(test_dish) > 0
    assert isinstance(test_dish, str)


def test_dish_description(fake):
    test_dish_description = fake.dish_description()
    assert len(test_dish_description) > 0
    assert isinstance(test_dish_description, str)


def test_ethnic_category(fake):
    test_ethnic_category = fake.ethnic_category()
    assert len(test_ethnic_category) > 0
    assert isinstance(test_ethnic_category, str)


def test_fruit(fake):
    test_fruit = fake.fruit()
    assert len(test_fruit) > 0
    assert isinstance(test_fruit, str)


def test_ingredient(fake):
    test_ingredient = fake.ingredient()
    assert len(test_ingredient) > 0
    assert isinstance(test_ingredient, str)


def test_measurement(fake):
    test_measurement = fake.measurement()
    assert len(test_measurement) > 0
    assert isinstance(test_measurement, str)


def test_metric_measurement(fake):
    test_metric_measurement = fake.metric_measurement()
    assert len(test_metric_measurement) > 0
    assert isinstance(test_metric_measurement, str)


def test_measurement_size(fake):
    test_measurement_size = fake.measurement_size()
    assert len(test_measurement_size) > 0
    assert isinstance(test_measurement_size, str)


def test_spice(fake):
    test_spice = fake.spice()
    assert len(test_spice) > 0
    assert isinstance(test_spice, str)


def test_sushi(fake):
    test_sushi = fake.sushi()
    assert len(test_sushi) > 0
    assert isinstance(test_sushi, str)


def test_vegetable(fake):
    test_vegetable = fake.vegetable()
    assert len(test_vegetable) > 0
    assert isinstance(test_vegetable, str)
