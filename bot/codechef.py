import requests
from bs4 import BeautifulSoup


def codechef_contest() :
    codechef_url = "https://www.codechef.com/contests"
    resp = requests.get(codechef_url).content
    soup = BeautifulSoup(resp, "lxml")

    # Extract the Present, Future and Past contests
    # Tables from the soup object

    tables = soup.find_all("table", {"class" : "dataTable"})

    present_contests_body = tables[0].find("tbody")
    present_contests = present_contests_body.find_all("tr")

    contests_string = "PRESENT CONTESTS\n\n"
    for contest in present_contests :
        contest_details = contest.find_all("td")
        contests_string += "Name: {}\n".format(contest_details[1].text)
        contests_string += "From: {}\n".format(contest_details[2].text)
        contests_string += "To: {}\n\n".format(contest_details[3].text)

    future_contests_body = tables[1].find("tbody")
    future_contests = future_contests_body.find_all("tr")

    contests_string += "\nFUTURE CONTESTS\n\n"
    for contest in future_contests :
        contest_details = contest.find_all("td")
        contests_string += "Name: {}\n".format(contest_details[1].text)
        contests_string += "From: {}\n".format(contest_details[2].text)
        contests_string += "To: {}\n\n".format(contest_details[3].text)

    return contests_string


def codechef_user(username):
    codechef_url = "https://www.codechef.com/users/" + username
    resp = requests.get(codechef_url)

    if resp.status_code != 200:
        return "User Not Found"

    soup = BeautifulSoup(resp.content, "lxml")

    user_profile = "Username: " + username

    # Get user's name
    user_details_div = soup.find('div', {"class": "user-details-container"})
    header = user_details_div.find('header')
    name = header.h2.text
    user_profile += "\nName: " + name

    # Get user's country
    country_span = soup.find('span', {"class": "user-country-name"})
    country = country_span.text
    user_profile += "\nCountry: " + country

    # Get user's Ratings
    rating_div = soup.find('a', {"class": "rating"})
    rating = rating_div.text
    user_profile += "\nOverall Rating: " + rating

    # Get user's Global and Country Rank
    sidebar = soup.find('div', {"class": "rating-ranks"})
    a_list = sidebar.find_all('a')
    user_profile += "\nGlobal Rank: " + a_list[0].strong.text
    user_profile += "\nCountry Rank: " + a_list[1].strong.text

    user_profile += "\n"
    return user_profile




