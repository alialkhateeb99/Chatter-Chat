# mocked_unit_tests.py

import sys

sys.path.append("..")

import unittest
from botfunctions import *
import botfunctions
import requests
from unittest import mock

KEY_INPUT = ""
KEY_EXPECTED = ""


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class FunTranslateTestCases(unittest.TestCase):
    def mocked_api_call(self, message):
        return MockResponse({KEY_EXPECTED: "is a boss, Ali Alkhateeb"}, 200)

    def setUp(self):
        self.success_test_params_funtranslate = [
            {
                KEY_INPUT: "Ali alkhateeb is a boss",
                KEY_EXPECTED: "is a boss, Ali Alkhateeb",
            }
        ]

    def test_funtranslate_bot_success(self):
        for test in self.success_test_params_funtranslate:
            with mock.patch("requests.post", self.mocked_api_call):
                json_data = test[KEY_INPUT]
                expected = test[KEY_EXPECTED]
                self.assertEqual(json_data, expected)


if __name__ == "__main__":
    unittest.main()
