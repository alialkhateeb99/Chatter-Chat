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
        self.success_test_params_get_bot_info = [ 
            {
                KEY_INPUT : "!! owner",
                KEY_EXPECTED: {
                    KEY_IS_BOT_COMMAND : True,
                    KEY_BOT_COMMAND : "owner",
                    KEY_BOT_RESULT : "Ali Alkhateeb is the owner of the site!!"
                }
            }
        ]
        self.failure_test_params_get_bot_info = [ 
            {
                KEY_INPUT : "!! helps",
                KEY_EXPECTED: {
                    KEY_IS_BOT_COMMAND : False,
                    KEY_BOT_COMMAND : "help",
                    KEY_BOT_RESULT : ""
                }
            }
        ]
        self.success_test_params_bot_command_helper = [
            {
                KEY_INPUT: "about",
                KEY_EXPECTED : 
                "Hello! Welcome to Ali's chat room! I am here to assist" + \
                " you! For a list of commands type '!! help' "
                
            }
        ]
        self.failure_test_params_bot_command_helper = [
            {
                KEY_INPUT: "about",
                KEY_EXPECTED : 
                "about"
                
            }
        ]
        self.success_test_check_message_image = [
            {
                KEY_INPUT: "https://www.extremetech.com/wp-content/uploads/2019/12/SONATA-hero-option2-764A4983-640x354.jpg",
                KEY_EXPECTED : 
                "<img src='https://www.extremetech.com/wp-content/uploads/2019/12/SONATA-hero-option2-764A4983-640x354.jpg' width='200' height='200' >"
                
            }
        ]
        self.failure_test_check_message_image = [
            {
                KEY_INPUT: "https://www.extremetech.com/wp-content/uploads/2019/12/SONATA-hero-option2-764A4983-640x354.jpg",
                KEY_EXPECTED : 
                "https://www.extremetech.com/wp-content/uploads/2019/12/SONATA-hero-option2-764A4983-640x354.jpg"
                
            }
        ]
        self.success_test_check_url_extension = [
            {
                KEY_INPUT: "https://www.extremetech.com/wp-content/uploads/2019/12/SONATA-hero-option2-764A4983-640x354.jpg",
                KEY_EXPECTED : True
                
            }
        ]
        self.failure_test_check_url_extension = [
            {
                KEY_INPUT: "https://www.extremetech.com/wp-content/uploads/2019/12/SONATA-hero-option2-764A4983-640x354.jpg",
                KEY_EXPECTED : False
            }
        ]
    def test_check_url_extension_success(self):
        for test in self.success_test_check_url_extension:
            response = check_url_extension(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            self.assertEqual(response,expected)
    def test_check_url_extension_failure(self):
        for test in self.failure_test_check_url_extension:
            response = check_url_extension(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            self.assertNotEqual(response,expected)
    
    
    def test_check_message_image_success(self):
        for test in self.success_test_check_message_image:
            response = check_message_image(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response,expected)
            
    def test_check_message_image_failure(self):
        for test in self.failure_test_check_message_image:
            response = check_message_image(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertNotEqual(response,expected)
        
    def test_get_bot_info_success(self):
        for test in self.success_test_params_get_bot_info:
            response = get_bot_info(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response[KEY_IS_BOT_COMMAND], expected[KEY_IS_BOT_COMMAND])
            self.assertEqual(response[KEY_BOT_COMMAND], expected[KEY_BOT_COMMAND])
            self.assertEqual(response[KEY_BOT_RESULT], expected[KEY_BOT_RESULT])
            self.assertDictEqual(response, expected)
            
    def test_get_bot_info_failure(self):
        for test in self.failure_test_params_get_bot_info:
            response = get_bot_info(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertNotEqual(response[KEY_IS_BOT_COMMAND], expected[KEY_IS_BOT_COMMAND])
            self.assertNotEqual(response[KEY_BOT_COMMAND], expected[KEY_BOT_COMMAND])
            self.assertNotEqual(response[KEY_BOT_RESULT], expected[KEY_BOT_RESULT])
            
    def test_bot_command_helper_success(self):
        for test in self.success_test_params_bot_command_helper:
            response = bot_command_helper(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response,expected)
    def test_bot_command_helper_failure(self):
        for test in self.failure_test_params_bot_command_helper:
            response = bot_command_helper(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertNotEqual(response,expected)
    
            
        
if __name__ == '__main__':
    unittest.main()