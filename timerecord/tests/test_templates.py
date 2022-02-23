# TODO Add Client for testing - work of all key pages

import unittest
from django.test import TestCase, Client

class URLTests(TestCase):

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)