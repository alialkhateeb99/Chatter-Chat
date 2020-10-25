#botfunctions.py
import requests

list_of_commands = ["about","help","funtranslate","owner"]

def get_bot_info(message):
    if message == '':
        return -1
        
    splitted_message = message.split()
    if splitted_message[0] == "!!":
        command_name = splitted_message[1]

        if command_name in list_of_commands:
            
            actual_message = " ".join(splitted_message[2:])
            
            if command_name == "about" or command_name == "help" or command_name == "owner":
                return bot_command_helper(command_name)
                
            if command_name == "funtranslate":
                return bot_command_funtranslate(actual_message)
        else:
            return "The command is not recognized by the bot!"
    else:
        return -1

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
        about_text = "Hello! Welcome to Ali's chat room! I am here to assist"
        about_text += " you! For a list of commands type '!! help' "
        return about_text
    elif command == "help":
        help_text =  " '!! about' for a brief description about the chat room."
        help_text += " '!! help' for a list of supported commands."
        help_text += " '!! funtranslate' to translate a message to a fun language!"
        help_text += " '!! owner' to see the owner of the site!"
        return help_text
    elif command == "owner":
        owner = "Ali Alkhateeb is the owner of the site!!"
        return owner


    
list_of_images_extensions = ["jpg","png","gif"]

def check_message_image(message):
    image_extension = message[-3:].lower()
    if image_extension in list_of_images_extensions:
        image_url = "<img src='" + message + "' width='200' height='200' >"
        return image_url
    else:
        return -1
        