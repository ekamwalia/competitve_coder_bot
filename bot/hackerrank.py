import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse


def hackerrank_contest():
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


def hackerrank_user(username):
    hackerrank_url = "https://www.hackerrank.com/" + username
    resp = requests.get(hackerrank_url)
    soup = BeautifulSoup(resp.content, "lxml")

    print(soup.prettify())
    user_profile = "Username: " + username

    # Get user's name

   # name_tag = soup.find('h3', {"itemprop": "name"})
    #print(name_tag.prettify())
    #name = name_tag.text
    #user_profile += "\nName: " + name

    # Get user's country
   # country_span = soup.find('span', {"class": "user-country-name"})
   # country = country_span.text
   # user_profile += "\nCountry: " + country

    # Get user's Ratings
    rating_span = soup.find('span', {"id": "hacker-contest-score"})
    rating = rating_span.text
    user_profile += "\nContest Rating: " + rating

    percentile_span = soup.find('span', {"id": "hacker-percentile"})
    percentile = percentile_span.text
    user_profile += "\nPrecentile " + percentile

    competitions_span = soup.find('span', {"id": "hacker-competitions"})
    competitions = competitions_span.text
    user_profile += "\nCompetitions: " + competitions

    user_profile += "\n"
    return user_profile


if __name__ == "__main__":
    print(hackerrank_user("ekamwalia"))



