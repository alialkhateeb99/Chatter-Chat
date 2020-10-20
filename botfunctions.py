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
            
            if command_name == "about":
                about_text = "Hello! Welcome to Ali's chat room! I am here to assist\n"
                about_text += " you with! For a list of commands type <!! help> "
                return about_text
            if command_name == "help":
                help_text = " <!! about> for a brief description about the chat room.\n"
                help_text += "<!! help> for a list of supported commands.\n"
                help_text += "<!! funtranslate> to translate a message to a fun language!"
                help_text += "<!! owner> to see the owner of the site!"
                return help_text
            if command_name == "funtranslate":
                try:
                    data = {
                        'text': actual_message
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
            if command_name == "owner":
                owner = "Ali Alkhateeb is the owner of the site!"
                return owner
                
            
        else:
            return "The command is not recognized by the bot!"
    else:
        return -1
    
list_of_images_extensions = ["jpg","png","gif"]

def check_message_image(message):
    image_extension = message[-3:].lower()
    if image_extension in list_of_images_extensions:
        image_url = "<img src='" + message + " width='200' height='200' >"
        return image_url
    else:
        return -1
        