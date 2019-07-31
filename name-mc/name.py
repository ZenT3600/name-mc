from bs4 import BeautifulSoup as bs
import requests


def is_available(name):
    url = "https://namemc.com/search?q=" + name
    page = requests.get(url).text
    soup = bs(page, "html.parser")
    x = soup.find_all("strong")[0]
    status = x.find_next("div").text
    if status == "Unavailable":
        return False
    elif status == "Available*":
        return True
    elif status == "Too Long":
        return "Too Long"
    elif status == "Invalid Characters":
        return "Invalid Characters"


def monthly_searches(name):
    url = "https://namemc.com/search?q=" + name
    page = requests.get(url).text
    soup = bs(page, "html.parser")
    x = soup.find_all("strong")[1]
    searches = x.find_next("div").text
    return searches


def matching_uuid(name):
    url = "https://namemc.com/search?q=" + name
    page = requests.get(url).text
    soup = bs(page, "html.parser")
    try:
        x = soup.find_all("h3", class_="mb-0")[0]
        uuid = x.find_next("samp").text
        return uuid
    except Exception as e:
        return False
