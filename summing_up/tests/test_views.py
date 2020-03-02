from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from add_numbers import views
import json
import ast


class TestModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.total_url = reverse('total')
        self.new_list_url = reverse('new_list')
        self.positive_message = "list of numbers was successfully stored"
        self.error_message = "Invalid list of numbers. Please post a simple list of numbers for Python 3 to read"

    def test_summing_up_GET(self):
        response = self.client.get(self.total_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"total": 50000005000000}')

    def test_create_list_of_numbers_POST_not_valid_list(self):
        post_body = {"key": "list(range(10000001))"}    # ast.literal_eval is used and so this is not accepted list
        response = self.client.post(self.new_list_url, post_body, content_type="application/json")
        content = json.loads(response.content)
        response_message = next(iter(content.values()))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.error_message, response_message)

    def test_create_list_of_numbers_POST_a_tuple(self):
        post_body = {"key": "(1,2)"}
        response = self.client.post(self.new_list_url, post_body, content_type="application/json")
        content = json.loads(response.content)
        response_message = next(iter(content.values()))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.error_message, response_message)

    def test_create_list_of_numbers_POST_list_with_non_numerical_elements(self):
        post_body = {"key": "[1,2,'a']"}
        response = self.client.post(self.new_list_url, post_body, content_type="application/json")
        content = json.loads(response.content)
        response_message = next(iter(content.values()))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.error_message, response_message)

    def test_create_list_of_numbers_POST_valid_list(self):
        post_body = {"key": "[1.5, 1, 0]"}
        response = self.client.post(self.new_list_url, post_body, content_type="application/json")
        content = json.loads(response.content)
        response_message = next(iter(content.values()))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.positive_message, response_message)



