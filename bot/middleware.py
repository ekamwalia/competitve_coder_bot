from bot.codechef import codechef_scraper
from bot.hackerrank import hackerrank_scraper
import string


def switch(message):
    arguements = message.split(' ')
    arg_count = len(arguements)
    command = arguements[0].lower()
    response = ''

    if (command == 'codechef' or command == '/codechef') and arg_count == 1:
        response = codechef_scraper()
    elif (command == 'hackerrank' or commands == '/hackerrank') and arg_count == 1:
        response = hackerrank_scraper()
    else:
        response = "Invalid command"

    return response