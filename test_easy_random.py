from easy_random import next_object
from test_models.customer import Customer


class TestEasyRandom:

    def test_return_random_values_for_string(self):
        data = next_object(Customer)

        assert data.name.strip() != ""

    def test_return_random_values_for_int(self):
        data = next_object(Customer)

        assert data.age != 0

