'''
#mocked_unit_tests.py
This file is for mocked unit tests
and API calls.
'''

import sys
sys.path.append("..")

import unittest
from unittest import mock

KEY_INPUT = ""
KEY_EXPECTED = ""

class MockResponse:
    '''
    This class defines the MockResponse
    generated by the mock api call
    '''
    def __init__(self,json_data,status_code):
        self.json_data = json_data
        self.status_code = status_code
    def json(self):
        ''' returns json_data '''
        return self.json_data


class FunTranslateTestCases(unittest.TestCase):
    ''' Defines mock api call and test params '''
    @classmethod
    def mocked_api_call(cls):
        ''' returns mock response '''
        return MockResponse({KEY_EXPECTED: "is a boss, Ali Alkhateeb"},200)
    def setUp(self):
        self.success_test_params_funtranslate = [
            {
                KEY_INPUT: "Ali alkhateeb is a boss",
                KEY_EXPECTED : "is a boss, Ali Alkhateeb"
            }
        ]

    def test_funtranslate_bot_success(self):
        ''' runs the test cases in params '''
        for test in self.success_test_params_funtranslate:
            with mock.patch('requests.post', self.mocked_api_call):
                json_data = test[KEY_INPUT]
                expected =  test[KEY_EXPECTED]
                self.assertEqual(json_data,expected)


if __name__ == '__main__':
    unittest.main()
