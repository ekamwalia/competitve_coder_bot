from bot.codechef import codechef_scraper
from bot.hackerrank import hackerrank_scraper
import string


def switch(message):
    arguements = message.split(' ')
    arg_count = len(arguements)
    command = string.lower(arguements[0])
    response = ''

    if command == 'codechef' and arg_count == 1:
        response = codechef_scraper()
    elif command == 'codechef' and arg_count == 1:
        response = hackerrank_scraper()
    else:
        response = "Invalid command"

    return response