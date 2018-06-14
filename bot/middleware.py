from bot.codechef import *
from bot.hackerrank import *
from bot.ctftime import *

def switch(message):
    arguments = message.split(' ')
    arg_count = len(arguments)
    command = arguments[0].lower()
    response = ''

    try:

        if command == '/start':
            response = start_message()
        elif (command == 'codechef' or command == '/codechef') and arg_count == 1:
            response = codechef_contest()
        elif (command == 'hackerrank' or command == '/hackerrank') and arg_count == 1:
            response = hackerrank_contest()
        elif command == 'codechef':
            response = codechef_user(arguments[1])
        elif command == 'hackerrank':
            response = hackerrank_user(arguments[1])
        elif (command == 'ctftime' or command == '/ctftime') and arg_count == 1:
            response = ctftime_contest()
        else:
            response = "Invalid command"
    
    except:
        response = "An unknown error occured. Please try again later"

    return response


def start_message():
    return "Greetings from Competitve Coder Bot!\nYou can use one of the quick commands to view the upcoming contests on a platform.\nYou can also text me with the name of a platform and a username to view a user's profile."