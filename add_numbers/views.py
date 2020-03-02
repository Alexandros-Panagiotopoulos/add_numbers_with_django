from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
import ast

# from summing_up.models import ListsOfNumbers
from summing_up.models import SumUpNumbers


@api_view(['POST'])
def create_list_of_numbers(request):
    body_unicode = request.body
    body = json.loads(body_unicode)
    string_to_list = next(iter(body.values()))
    number_list = get_list_from_string(string_to_list)
    is_valid = check_if_list_is_valid(number_list)
    if not is_valid:
        message = {
            "title": 'Invalid list of numbers. Please post a simple list of numbers for Python 3 to read',
            "status": 400
        }
        return HttpResponse(json.dumps(message), status=400)

    # Code to save the list in the database ListsOfNumbers
    message = {"title": 'list of numbers was successfully stored', "status": 200}
    return HttpResponse(json.dumps(message))


def get_list_from_string(string_to_list):
    try:
        number_list = ast.literal_eval(string_to_list)
        # If client is trusted then eval(string_to_list) can be used to handle complex methods like "list(range(10))"
        return number_list
    except ValueError:
        return None


def check_if_list_is_valid(number_list):
    if not all([number_list, isinstance(number_list, list)]):
        return False
    elif not all(isinstance(x, (int, float)) for x in number_list):
        return False
    else:
        return True


def summing_up(request):
    numbers_to_add = list()

    # code to retrieve the list from the database

    if not numbers_to_add:
        numbers_to_add = get_hardcoded_list()
    sum_up = SumUpNumbers(numbers_to_add)
    summary = sum_up.get_the_sum()
    return HttpResponse(json.dumps({"total": summary}))


def get_hardcoded_list():
    numbers_to_add = list(range(10000001))
    return numbers_to_add
