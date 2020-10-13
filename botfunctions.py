#botfunctions.py
import requests

list_of_commands = ["about","help","funtranslate"]

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
                about_text += " you with! For a list of commands type '!! help' "
                return about_text
            if command_name == "help":
                help_text = "'!! about' for a brief description about the chat room\n"
                help_text += "'!! help' for a list of supported commands\n"
                help_text += "'!! funtranslate' to translate a message to a fun language!"
                return help_text
            if command_name == "funtranslate":
                # data = {
                # 'text': actual_message
                # }
                # response = requests.post('https://api.funtranslations.com/translate/yoda.json', data=data)
                # print(response)
                print("TODOOOOOO")
            
            
        else:
            return "The command is not recognized by the bot!"
    else:
        return -1
    
