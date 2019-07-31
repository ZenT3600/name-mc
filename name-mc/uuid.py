from bs4 import BeautifulSoup as bs
import requests


# https://namemc.com/profile/UUIDq=UUID

def matching_name(uuid):
    url = "https://namemc.com/profile/" + uuid + "?q=" + uuid
    page = requests.get(url).text
    soup = bs(page, "html.parser")
    try:
        x = soup.find_all("hr", class_="mt-1")[0]
        name = x.find_previous("h1").text
        return name
    except Exception as e:
        return False
