from django.db import models


# class ListsOfNumbers(models.Model):
#     # Code to create the database
#     pass


class SumUpNumbers:

    def __init__(self, numbers_to_add):
        self.numbers_to_add = numbers_to_add

    def get_the_sum(self):
        summary = 0
        for number in self.numbers_to_add:
            summary += number
        return summary

