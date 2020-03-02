from django.test import TestCase
from summing_up.models import SumUpNumbers

import math


class TestModels(TestCase):

    def test_summing_list_of_integers_and_floats(self):
        numbers_to_add = [0, -1, -1.1]
        sum_up = SumUpNumbers(numbers_to_add)
        summary = sum_up.get_the_sum()

        self.assertEqual(summary, -2.1)

    def test_summing_list_of_real_numbers(self):
        numbers_to_add = [math.e, math.pi]
        sum_up = SumUpNumbers(numbers_to_add)
        summary = sum_up.get_the_sum()

        self.assertEqual(summary, math.pi+math.e)

    def test_summing_large_list_with_large_sum(self):
        numbers_to_add = list(range(10000001))
        sum_up = SumUpNumbers(numbers_to_add)
        summary = sum_up.get_the_sum()

        self.assertEqual(summary, 50000005000000)
