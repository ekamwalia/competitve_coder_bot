import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse


def hackerrank_scraper():
    hackerrank_url = "https://www.hackerrank.com/contests"
    resp = requests.get(hackerrank_url)
    soup = BeautifulSoup(resp.content, "lxml")
    # Extract the Present, Future and Past contests
    # Tables from the soup object

    contests_list = soup.find_all("div", {"class": "contest-tab-expander", "data-contest-state": "Active"})
    contests_string = "UPCOMING CONTESTS\n\n"
    count_contests = len(contests_list)

    for contest in range(1, count_contests):
        contest_details = contests_list[contest].contents

        contests_string += "Name: " + contest_details[0].span.text + "\n"

        # Get startTime from meta tag and then parse ISO 8601
        time_meta = contest_details[1].find('meta', {"itemprop": "startDate"})
        time_comp = parse(time_meta['content']).isoformat(' ')
        time = time_comp.split('+')[0]
        contests_string += "From: " + time + "\n"

        # # Get startTime from meta tag and then parse ISO 8601
        time_meta = contest_details[1].find('meta', {"itemprop": "endDate"})
        time_comp = parse(time_meta['content']).isoformat(' ')
        time = time_comp.split('+')[0]
        contests_string += "To: " + time + "\n\n"

    return contests_string
