from easy_random import next_object
from test_models.customer import Customer


class TestEasyRandom:

    def test_return_random_values(self):
        data = next_object(Customer)

        assert data.name is not None and data.name.strip() is not ""
