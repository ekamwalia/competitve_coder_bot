import requests
from bs4 import BeautifulSoup

def Codechef_scraper() :
    codechef_url = "https://www.codechef.com/contests"
    resp = requests.get(codechef_url).content
    soup = BeautifulSoup(resp, "lxml")

    # Extract the Present, Future and Past contests
    # Tables from the soup object

    tables = soup.find_all("table", {"class" : "dataTable"})

    present_contests_body = tables[0].find("tbody")
    present_contests = present_contests_body.find_all("tr")

    contests_list = "PRESENT CONTESTS\n\n"
    for contest in present_contests :
        contest_details = contest.find_all("td")
        contests_list += "Name: " + contest_details[1].text + "\n"
        contests_list += "From: " + contest_details[2].text + "\n"
        contests_list += "To: " + contest_details[3].text + "\n\n"

    future_contests_body = tables[1].find("tbody")
    future_contests = future_contests_body.find_all("tr")

    contests_list += "\nFUTURE CONTESTS\n\n"
    for contest in future_contests :
        contest_details = contest.find_all("td")
        contests_list += "Name: " + contest_details[1].text + "\n"
        contests_list += "From: " + contest_details[2].text + "\n"
        contests_list += "To: " + contest_details[3].text + "\n\n"

    return contests_list
