#botfunctions.py
import requests

list_of_commands = ["about","help","funtranslate","owner"]

KEY_IS_BOT_COMMAND = "is_bot"
KEY_BOT_COMMAND = "bot_command"
KEY_BOT_RESULT = "bot_result"

def get_bot_info(message):
    if message == '':
        return {
            KEY_IS_BOT_COMMAND: False,
            KEY_BOT_COMMAND: "",
            KEY_BOT_RESULT: -1
        }
        
    splitted_message = message.split()
    if check_valid_bot_command(message) and splitted_message[0] == "!!":
        command_name = splitted_message[1]

        if command_name in list_of_commands:
            
            actual_message = " ".join(splitted_message[2:])
            
            if command_name == "about" or command_name == "help" or command_name == "owner":
                result = bot_command_helper(command_name)
                return {
                    KEY_IS_BOT_COMMAND : True,
                    KEY_BOT_COMMAND : command_name,
                    KEY_BOT_RESULT: result
                }
            if command_name == "funtranslate":
                result = bot_command_funtranslate(actual_message)
                return {
                    KEY_IS_BOT_COMMAND: True,
                    KEY_BOT_COMMAND : command_name,
                    KEY_BOT_RESULT: result
                }
        else:
            return {
                KEY_IS_BOT_COMMAND: True,
                KEY_BOT_COMMAND: "",
                KEY_BOT_RESULT :"The command is not recognized by the bot!"
            }
    else:
        return {
            KEY_IS_BOT_COMMAND: False,
            KEY_BOT_COMMAND: "",
            KEY_BOT_RESULT : "No command entered"
        }

def bot_command_funtranslate(message):
    try:
        data = {
            'text': message
        }
        headers = {
            'X-Funtranslations-Api-Secret': '',
        }
        response = requests.post('https://api.funtranslations.com/translate/yoda.json',headers=headers, data=data)
        data = response.json()
        translated = data["contents"]["translated"]
    except:
        return "No api calls left for the bot! give it some time."
    return translated
        
def bot_command_helper(command):
    if command == "about":
        about_text = "Hello! Welcome to Ali's chat room!"
        return about_text
    elif command == "help":
        help_text =  " '!! about' for a brief description about the chat room."
        return help_text
    elif command == "owner":
        owner = "Ali Alkhateeb is the owner of the site!!"
        return owner

def check_valid_bot_command(message):
    splitted_message = message.split()
    if len(splitted_message) > 1:
        return True
    else:
        return False
    
list_of_images_extensions = ["jpg","png","gif"]


def check_url_extension(url):
    image_extension = url[-3:].lower()
    if image_extension in list_of_images_extensions:
        return True
    else: 
        return False

def check_message_image(message):
    if check_url_extension(message) == True:
        image_url = "<img src='" + message + "' width='200' height='200' >"
        return image_url
    else:
        return -1
        
