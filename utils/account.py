from bs4 import BeautifulSoup as bs
import requests


def get_previous_names(profile):
    url = "https://namemc.com/profile/" + profile
    page = requests.get(url).text
    soup = bs(page, "html.parser")
    name_object = soup.find_all(attrs={"translate": "no"})
    names = []
    for i in range(0, len(name_object)):
        if name_object[i].has_attr("href"):
            names.append(name_object[i].text)
        else:
            pass
    if names:
        return names
    elif not names:
        return False


def get_head_command(profile):
    url = "https://namemc.com/profile/" + profile
    page = requests.get(url).text
    soup = bs(page, "html.parser")
    command_object = soup.find_all("input", attrs={"class": "form-control", "readonly": "", "style": "font-family: Consolas, monospace;"})
    commands = []
    for i in range(0, len(command_object)):
        commands.append(command_object[i].get("value"))
    if commands:
        return commands
    elif not commands:
        return False
