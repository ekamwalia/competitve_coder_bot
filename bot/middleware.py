from bot.codechef import *
from bot.hackerrank import *


def switch(message):
    arguments = message.split(' ')
    arg_count = len(arguments)
    command = arguments[0].lower()
    response = ''

    if (command == 'codechef' or command == '/codechef') and arg_count == 1:
        response = codechef_contest()
    elif (command == 'hackerrank' or command == '/hackerrank') and arg_count == 1:
        response = hackerrank_contest()
    elif command == 'codechef':
        response = codechef_user(arguments[1])
    elif command == 'hackerrank':
        response = hackerrank_user(arguments[1])
    else:
        response = "Invalid command"

    return response
