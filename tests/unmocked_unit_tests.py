#unmocked_unit_tests.py

import sys
sys.path.append("..")

import unittest
from botfunctions import *
import botfunctions

KEY_INPUT = "input"
KEY_EXPECTED = "expected"

class ChatRoomTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [ 
            {
                KEY_INPUT : "!! owner",
                KEY_EXPECTED: {
                    KEY_IS_BOT_COMMAND : True,
                    KEY_BOT_COMMAND : "owner",
                    KEY_BOT_RESULT : "Ali Alkhateeb is the owner of the site!!"
                }
            }
            
            
        ]
        
        
        
        
        
    def test_get_bot_info_success(self):
        for test in self.success_test_params:
            response = get_bot_info(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response[KEY_IS_BOT_COMMAND], expected[KEY_IS_BOT_COMMAND])
            self.assertEqual(response[KEY_BOT_COMMAND], expected[KEY_BOT_COMMAND])
            self.assertEqual(response[KEY_BOT_RESULT], expected[KEY_BOT_RESULT])
            
        
if __name__ == '__main__':
    unittest.main()