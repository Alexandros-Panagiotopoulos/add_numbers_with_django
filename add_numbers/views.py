from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
import ast


@api_view(['POST'])
def create_list_of_numbers(request):
    body_unicode = request.body
    body = json.loads(body_unicode)
    string_to_list = next(iter(body.values()))
    number_list = ast.literal_eval(string_to_list)
    is_valid = check_if_list_is_valid(number_list)
    if not is_valid:
        message = {
            "title": 'Invalid list of numbers. Please post a valid list of numbers for Python 3 to read or create',
            "status": 400
        }
        return HttpResponse(json.dumps(message), status=400)

    # Code to store the list in the database

    return HttpResponse('list of numbers was successfully stored')


def check_if_list_is_valid(number_list):
    return False


def summing_up(request):
    a = 10
    return HttpResponse(json.dumps({"total": a}))
